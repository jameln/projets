# -*- coding: utf-8 -*-
{
    'name': "T-Jara",

    'summary': """
        Solution pour la gestion de l'activité commerciale d'une entreprise (PME)""",

    'description': """
        Le module T-Jara est une solution compacte et performante pour la gestion de l'activité commerciale d'une petite ou moyenne entreprise (PME)
    """,

    'author': "Khidma",
    'website': "http://www.khidma.tn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','report'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/acces_rules.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/facture.xml',
        'views/produit.xml',
        'views/cron.xml',
        'report/report_facture_template.xml',
        'report/report_facture.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}
