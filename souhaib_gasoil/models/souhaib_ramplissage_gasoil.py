from odoo import models, fields, api

class souhaibGasoilRemplissage(models.Model):
    _name = 'souhaib.gasoil.remplissage'
    name = fields.Char(string='Name')

    date = fields.Datetime(string='Date')
    remarque = fields.Text(string='remarque')
    vehicule_id = fields.Many2one('fleet.vehicle', string="Voiture", required=True)
    product_id = fields.Many2one('product.product', string="Article", required=True)
    line_ids = fields.One2many('souhaib.gasoil.remplissage.line', 'remplissage2_id', string='Lines')
    count_pickings = fields.Integer(string ="Number de trf ")
    picking_ids = fields.Many2many('stock.picking', string='Transferts')
    quantity_prevu = fields.Integer(string='Quantity Prevu')
    quantity_total = fields.Integer(string='Quantité',compute='_compute_quantity_remplissage')
    
    date_prevu = fields.Datetime(string='Date prévue')


    state = fields.Selection([('draft', 'Brouillon'), ('done', 'Terminer')], default='draft')


    def confirm_remplissage(self):
        for rec in self:
            rec.state = 'done'

        if rec.date == False:
            rec.date = fields.Datetime.now()
        for line in rec.line_ids:
            if line.quantity > 0:
                res = {
                    'stock_remplissage_id': rec._origin.id,
                    # 'purchase_id': rec.purchase_order_id.id,
                    'picking_type_id': self.env['stock.picking.type'].search(
                        [('code', '=', 'incoming')], limit=1).id,
                    'date': fields.Datetime.now(),
                    'location_id': 8,
                    'location_dest_id': line.citerne.id,
                }
                picking = self.env['stock.picking'].create(res)
                line.picking_id = picking
                rec.picking_ids = [(4, picking.id)]
                rec.count_pickings = len(rec.picking_ids)
                #
                # self.env['stock.move'].create(
                #     {'picking_id': picking.id,
                #      'product_id': rec.product_id.id,
                #      'purchase_line_id': rec.purchase_order_id.order_line[0].id,
                #      'name': rec.name,
                #      'product_uom_qty': line.quantity,
                #      'quantity_done': line.quantity,
                #      'product_uom': rec.product_id.uom_id.id,
                #      'location_id': picking.location_id.id,
                #      'location_dest_id': picking.location_dest_id.id})
    

    def draft_remplissage(self):
        for rec in self:
            rec.state = 'draft'


    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('remplissage_sequence')
        res = super().create(vals)
        return res
    @api.depends('line_ids')
    def _compute_quantity_remplissage(self):
        for rec in self:
            rec.quantity_total = sum(rec.line_ids.mapped('quantity'))




    class souhaibGasoilRemplissageLine(models.Model):



         _name = 'souhaib.gasoil.remplissage.line'

         name = fields.Char(string='name', compute='compute_name')
         remplissage2_id = fields.Many2one('souhaib.gasoil.remplissage', string='remplissage Gasoil')
         quantity = fields.Integer(string='Quantité')
         citerne = fields.Many2one('stock.location', string="Citerne", required=True)
         picking_id = fields.Many2one('stock.picking', string='Transfert')


        