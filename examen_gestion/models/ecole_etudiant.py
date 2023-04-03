from odoo import models, fields, api
from odoo.exceptions import UserError

class EcoleEtudiantt(models.Model):
    _inherit = 'res.partner'




    is_citerne = fields.Boolean(string='Est Etudiantt ?')
    cnee = fields.Char(string='CNE')
  

    


   