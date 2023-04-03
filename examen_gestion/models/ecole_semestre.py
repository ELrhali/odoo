from odoo import fields, models, api, _


class EcoleSemestre(models.Model):
    _name = 'ecole.semestre'

    name = fields.Char(string='Nom ', required=True, help="Nom de la Semestre ")
    date_debut = fields.Date(Srting='Date de début ')
    date_fin = fields.Date(Srting='Date de fin ')
    date = fields.Datetime(string="Exam Date")
    location = fields.Char(string="Location")
    description = fields.Text(string='Description')

