# -*- coding: utf-8 -*-
{
    'name': "Man Gasaoil",

    'summary': """
        Gestions de remplisage de gasaoil
        Gestion des citernes
        Gestion de ravitaillement """,

    'description': """
        Ce module se caracterise par des la gestion de ravitaillement, la remplisage de gasoil, gestion des citernes, la consomation des gasoil au  niveau des vehicule 
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
        'data/ir_sequence_data.xml',
        'views/souhaib_ravitaillement.xml',
        'views/souhaib_remplissage.xml',
        'views/souhaib_stock_location.xml',
        'views/souhaib_product_template.xml',
        'views/souhaib_purchase_order.xml',

        #
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
    'application':True,
        'sequence':-100,

}