from odoo import fields, models, api, _


class EcoleSession(models.Model):
    _name = 'ecole.session'

    name = fields.Char(string='Nom ', required=True, help="Nom de la Session ")
    date_debut = fields.Date(Srting='Date de début ')
    date_fin = fields.Date(Srting='Date de fin ')
    state = fields.Selection([
        ('waiting', 'En attendant'),
        ('in_progress', 'En cours'),
        ('finished', 'terminé')
    ], string='State', default='waiting')
    student_count = fields.Integer(string='Nombre d étudiants')
   
    # student_count = fields.Integer(string='Nombre d\'étudiants inscrits', compute='_compute_student_count', store=True)

    # def _compute_student_count(self):
    #     for session in self:
    #         session.student_count = self.env['ecole.etudiant'].search_count([('session_id', '=', session.id)])