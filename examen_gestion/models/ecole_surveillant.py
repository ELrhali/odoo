
from odoo import fields, models, api


class EcoleSurveillant(models.Model):
    _name = 'ecole.surveillant'
    _inherit = ['mail.thread']
    _description = 'Enregistrement du personnel enseignant'



    def create_employee(self):
        """Création du personnel pour le personnel enseignant"""
        for rec in self:
            values = {
                'name': rec.name + rec.last_name,
                'gender': rec.gender,
                'birthday': rec.date_of_birth,
                'image_1920': rec.image,
                'work_phone': rec.phone,
                'work_email': rec.email,
            }
            emp_id = self.env['hr.employee'].create(values)
            rec.employee_id = emp_id.id



    name = fields.Char(string='Name', required=True,
                        help="Entrez le prénom")
    
    id_examen = fields.Many2one(  'ecole.examen',string='id examen')



    faculty_id = fields.Char(string="ID", readonly=True)
    last_name = fields.Char(string='Nom de famille', help="Entrez le nom de famille")
    image = fields.Binary(string="Image", attachment=True)
    email = fields.Char(string="Email",
                    help="Entrez l'email pour les contacts")
    phone = fields.Char(string="Téléphone",
                    help="Entrez le numéro de téléphone pour les contacts")
    mobile = fields.Char(string="Mobile",
                     help="Entrez le numéro de mobile pour les contacts")
    date_of_birth = fields.Date(string="Date de naissance", help="Entrez la date de naissance")


    employee_id = fields.Many2one('hr.employee', string="Employé associé")
    degree = fields.Many2one('hr.recruitment.degree', string="Diplôme",
                         Help="Sélectionnez votre diplôme le plus élevé")
    gender = fields.Selection(
         [('male', 'Masculin'), ('female', 'Féminin')],
         string='Sexe', required=True, default='male',
         track_visibility='onchange')
