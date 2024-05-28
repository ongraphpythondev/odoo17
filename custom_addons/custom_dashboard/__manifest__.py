# -*- coding: utf-8 -*-
{
    'name': "custom_dashboard",

    'summary': "Custom Dashboard by using owl js",

    'description': """
OWL Custom Dashboard
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web','sale','board'],
    'application': True,
    'installable': True,
    'auto_install': False,
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sales_dashboard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {    
        'web.assets_backend': [
        'custom_dashboard/static/src/components/**/*.js',
        'custom_dashboard/static/src/components/**/*.xml',
        'custom_dashboard/static/src/components/**/*.scss',
        'custom_dashboard/static/src/css/custom_style.css',
        ]
    }
}

