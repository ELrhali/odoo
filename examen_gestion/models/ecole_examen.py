from odoo import fields, models

class EcoleExamen(models.Model):
    _name = 'ecole.examen'



    cnee = fields.Many2one('res.partner', string='Nom d\'etudiant', required=True,domain=[('is_citerne', '=', True)])
    examen_name = fields.Char(string='ID')
    date = fields.Date(string='Date d\'examen')
   
    is_citerne = fields.Boolean(string='Est Etudiantt ?')
    annee_unv = fields.Many2one('ecole.anneeunv',
                                  string='Annee Universitaire',
                                  help="annee unv", required=True)
    
    session = fields.Many2one('ecole.session',
                                  string='sessionv', required=True)  
    matiere = fields.Many2one('ecole.matiere', 
                                  string='Matiere', required=True) 
    semestre = fields.Many2one('ecole.semestre',
                                  string='Semestre') 
    typeexamen = fields.Many2one('ecole.typeexamen',
                                  string='Type d\'examen') 
    


    sur_veillant = fields.One2many('ecole.surveillant','id_examen',string='Surveillant', required=True)

    # state = fields.Selection([('draft', 'Brouillon'), ('done', 'Terminer')], default='draft')

    











    
