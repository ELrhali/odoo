from odoo import models, fields

class EcoleTypeExamen(models.Model):
    _name = 'ecole.typeexamen'
    _description = 'Type Examen'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    duration = fields.Float(string='Duration (minutes)')
    question_count = fields.Integer(string='Number of Questions')
    points_per_question = fields.Float(string='Points per Question')
    minimum_grade = fields.Float(string='Minimum Grade')
    created_by = fields.Many2one('res.users', string='Created By', default=lambda self: self.env.uid)
    creation_date = fields.Date(string='Creation Date', default=fields.Date.today)