# -*- coding: utf-8 -*-
{
    'name': "custom_inventory",

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
    'depends': ['base','product','stock'],
    # 'qweb': [],
    'application': True,
    'installable': True,
    'auto_install': False,


    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/secuirty.xml',
        'views/views.xml',
        # 'views/store_man_dashboard_template.xml',
        'views/store_man_dashboard.xml',
        # 'views/templates.xml',
        # 'views/assets.xml',
    ],
    # 'assets': {    
    #     'web.assets_backend': [
    #     'custom_inventory/static/src/components/**/*.xml',
    #     'custom_inventory/static/src/components/**/*.js',
    #     ]
    # },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

