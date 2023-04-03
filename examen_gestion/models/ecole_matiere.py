from odoo import fields, models, api, _


class EcoleMatiere(models.Model):
    _name = 'ecole.matiere'

    name = fields.Char(string='Nom ', required=True, help="Nom de la matiere ")
    module = fields.Many2one('ecole.module',string='Module')
  
    code = fields.Integer(Srting='Code')

    description = fields.Text(string='Description')
