from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class souhaibGasoilRavitaillement(models.Model):
    _name = 'souhaib.gasoil.ravitaillement'
    name = fields.Char(string='Name')
    quantity_prevu = fields.Integer(string='Quantity Prevu')
    date = fields.Datetime(string='Date')
    date_prevu = fields.Datetime(string='Date prévue')
    quantity_total = fields.Integer(string='Quantité',compute='compute_quantity_ravitaillement')
    product_id = fields.Many2one('product.product', string="Article", required=True)
    remarque = fields.Text(string='remarque')
    state = fields.Selection([('draft', 'Brouillon'), ('done', 'Terminer')], default='draft')
    line_ids = fields.One2many('souhaib.gasoil.ravitaillement.line', 'ravitaillement_id', string='Lines')
    picking_ids = fields.Many2many('stock.picking', string='Transferts')
    count_pickings = fields.Integer(string='Count Picking')
    purchase_order_id = fields.Many2one('purchase.order', string='Bon de commande')

    @api.constrains('quantity_total')
    def _check_quantity_total(self):
        for rec in self:
            if rec.quantity_total > rec.quantity_prevu:
                raise ValidationError(
                    'Vous avez saisi une quntite de ravitaillement supérieur à celle de la quantité prévue')

    def action_view_pickings(self):
        if len(self.picking_ids.ids) > 0:
            result = {
                'name': "Transferts",
                'res_model': 'stock.picking',
                'view_type': 'form',
                'view_mode': 'tree,form',
                'domain': [('id', 'in', self.picking_ids.ids)],
                'type': 'ir.actions.act_window',
                'target': 'current',
            }
            return result
        else:
            raise UserError("Aucun Transfert n'est encore disponible")

    def confirm_ravitaillement(self):
        for rec in self:
            rec.state = 'done'

        if rec.date == False:
            rec.date = fields.Datetime.now()

        for line in rec.line_ids:
            if line.quantity > 0:
                res = {
                    'stock_ravitaillement_id': rec._origin.id,
                    'purchase_id': rec.purchase_order_id.id,
                    'picking_type_id': self.env['stock.picking.type'].search(
                        [('code', '=', 'incoming')], limit=1).id,
                    # 'partner_id': rec.client_id.id,
                    'date': fields.Datetime.now(),
                    # 'location_id': self.env.ref('stock.stock_location_stock').id,
                    # 'location_id': self.env['stock.location'].search([('barcode', '=', 'WH-STOCK')]).id,
                    'location_id': 8,
                    'location_dest_id': line.citerne.id,
                }
                picking = self.env['stock.picking'].create(res)
                line.picking_id = picking
                rec.picking_ids = [(4, picking.id)]
                rec.count_pickings = len(rec.picking_ids)
                #
                self.env['stock.move'].create(
                    {'picking_id': picking.id,
                     'product_id': rec.product_id.id,
                    #  'purchase_line_id': rec.purchase_order_id.order_line[0].id,
                     'name': rec.name,
                     'product_uom_qty': line.quantity,
                     'quantity_done': line.quantity,
                     'product_uom': rec.product_id.uom_id.id,
                     'location_id': picking.location_id.id,
                     'location_dest_id': picking.location_dest_id.id})

                picking.button_validate()

    def draft_ravitaillement(self):
        for rec in self:
            rec.state = 'draft'

    @api.depends('line_ids')
    def compute_quantity_ravitaillement(self):
        for rec in self:
            rec.quantity_total = sum(rec.line_ids.mapped('quantity'))

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('ravitaillement_sequence')
        res = super().create(vals)
        return res

class souhaibGasoilRavitaillementLine(models.Model):
    _name = 'souhaib.gasoil.ravitaillement.line'

    name = fields.Char(string='name', compute='compute_name')
    ravitaillement_id = fields.Many2one('souhaib.gasoil.ravitaillement', string='Ravitaillement Gasoil')
    quantity = fields.Integer(string='Quantité')
    citerne = fields.Many2one('stock.location', string="Citerne", required=True)
    picking_id = fields.Many2one('stock.picking', string='Transfert')
    # compteur = fields.Float(string='Compteur')
    # compteur_n_1 = fields.Float(string='Compteur n-1')
    # picking_id = fields.Many2one('stock.picking', string='Transfert')

    @api.constrains("quantity")
    def _check_quantity(self):
        for rec in self:
            if rec.quantity > rec.citerne.capacity:
                raise ValidationError(
                    "La capacité saisie dépasse la capacité maximal de la %s." % (rec.citerne.name))