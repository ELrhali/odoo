from odoo import models, fields, api, SUPERUSER_ID
from odoo.exceptions import UserError

class souhaibPurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    is_gasoil = fields.Boolean(string='Est gasoil', compute='compute_is_gasoil')
    souhaib_ravitaillement_ids = fields.Many2many('souhaib.gasoil.ravitaillement', string='Ravitaillement gasoil')
    count_ravitaillement = fields.Integer(string='Ravitaillements', compute='compute_ravitaillement')

    @api.depends('souhaib_ravitaillement_ids')
    def compute_ravitaillement(self):
        for rec in self:
            rec.count_ravitaillement = len(rec.souhaib_ravitaillement_ids)

    def action_view_ravitaillement(self):
        if len(self.souhaib_ravitaillement_ids.ids) > 0:
            result = {
                'name': "Ravitaillement gasoil",
                'res_model': 'souhaib.gasoil.ravitaillement',
                'view_type': 'form',
                'view_mode': 'tree,form',
                'domain': [('id', 'in', self.souhaib_ravitaillement_ids.ids)],
                'type': 'ir.actions.act_window',
                'target': 'current',
            }
            return result
        else:
            raise UserError("Aucun Ravitaillement n'est encore disponible")

    @api.depends('order_line', 'order_line.product_id')
    def compute_is_gasoil(self):
        for rec in self:
            is_gasoil = False
            for line in rec.order_line:
                if line.product_id.is_fuel == True:
                    is_gasoil = True
            rec.is_gasoil = is_gasoil

    def button_confirm(self):
        res = super(souhaibPurchaseOrder, self).button_confirm()
        for po in self:
            if po.is_gasoil == True:
                # for picking in po.picking_ids:
                #     picking.action_cancel()
                #     picking.unlink()
                for article in po.order_line.mapped('product_id'):
                    souhaib_gasoil_ravitaillement = self.env['souhaib.gasoil.ravitaillement'].create({'product_id': article.id, 'purchase_order_id': po.id, 'date_prevu': po.date_planned,
                                                                'quantity_prevu': sum(po.order_line.filtered(lambda x:x.product_id.id == article.id).mapped('product_qty'))})
                    for citerne in self.env['stock.location'].search([('is_citerne', '=', True)]):
                        self.env['souhaib.gasoil.ravitaillement.line'].create({'ravitaillement_id': souhaib_gasoil_ravitaillement.id, 'citerne': citerne.id})
                    po.souhaib_ravitaillement_ids = [(4, souhaib_gasoil_ravitaillement.id)]
        return res

    def button_cancel(self):
        result = super(ensaPurchaseOrder, self).button_cancel()
        for po in self:
            if po.is_gasoil == True:
                for ensa_ravitaillement_id in po.ensa_ravitaillement_ids:
                    ensa_ravitaillement_id.unlink()
        return result