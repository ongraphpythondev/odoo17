# -*- coding: utf-8 -*-
{
    'name': "E_commerce",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base','web','mail','board'],
    'application': True,
    'installable': True,
    'auto_install': False,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/dashboard_menu.xml',
        'views/orderview.xml',
        'views/menuaction.xml',
        'views/productview.xml',
        'views/cartview.xml',
        'views/counter.xml',
        # 'views/assets.xml',
        
        # 'views/templates.xml',
        
        
    ],
    'assets': {
        'web.assets_frontend': [
        #    'e_commerce/static/src/js/counter.js'
        #    'e_commerce/static/src/xml/custom_dashboard.xml'
           
        ],
        
        'web.assets_backend': [
        #    'e_commerce/static/src/js/counter.js'
        #    'e_commerce/static/src/xml/custom_dashboard.xml'
        ],
    }
}


