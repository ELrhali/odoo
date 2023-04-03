# -*- coding: utf-8 -*-
{
    'name': "Gestion des Examen",

    'summary': """
        Gestions de remplisage de gasaoil
        Gestion des etudiant
        Gestion de ravitaillement """,

    'description': """
        Ce module va gérer la gestion des examens 
    """,

    'author': "ENSA TANGER",
    'website': "http://www.ensatanger.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'purchase','fleet'],

    # always loaded
    'data': [

        'security/ir.model.access.csv',
       
        'views/ecole_etudiant.xml',
        'views/ecole_module.xml',
        'views/ecole_matiere.xml',
        'views/ecole_semestre.xml',
        'views/ecole_session.xml',
        'views/ecole_typeexamen.xml',
        'views/ecole_examen.xml',
        'views/ecole_anneeunv.xml',
        'views/ecole_surveillant.xml',

        
        # 'views/ecole_session.xml',


        
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
    'application':True,
    'sequence':-100,
    
}