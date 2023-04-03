from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_fuel = fields.Boolean(string='Est Fuel ?')

class ProductProduct(models.Model):
    _inherit = 'product.product'

    is_fuel = fields.Boolean(string='Est Fuel ?', related='product_tmpl_id.is_fuel')
