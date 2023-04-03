from odoo import models, fields, api
from odoo.exceptions import UserError

class souhaibStockLocation(models.Model):
    _inherit = 'stock.location'

    is_citerne = fields.Boolean(string='Est Citerne ?')
    capacity = fields.Integer(string='Capacité')
    # product_id = fields.Many2one('product.product', string="Article")
    compteur = fields.Float(string='Compteur')
