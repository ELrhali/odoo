from odoo import models, fields, api


class souhaibStockPicking(models.Model):
    _inherit = 'stock.picking'

    stock_ravitaillement_id = fields.Many2one('souhaib.gasoil.ravitaillement', string='Ravitaillement')
    stock_remplissage_id = fields.Many2one('souhaib.gasoil.remplissage', string='Remplissage')