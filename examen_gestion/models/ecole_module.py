from odoo import fields, models, api, _


class EcoleModule(models.Model):
    _name = 'ecole.module'

    name = fields.Char(string='Nom ', required=True, help="Nom de la module ")
    code = fields.Integer(Srting='Code')
    duree = fields.Float(string='Durée en heure')
    state = fields.Selection([('draft', 'Brouillon'), ('done', 'Terminer')], default='draft')
    description = fields.Text(string='Description')

