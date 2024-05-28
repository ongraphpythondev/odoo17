# -*- coding: utf-8 -*-
{
    'name': "todo_list",

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
    'depends': ['base'],
    'application': True,
    'installable': True,
    'auto_install': False,


    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/todo_list.xml'
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {    
        'web.assets_backend': [
        'todo_list/static/src/components/*/*.js',
        'todo_list/static/src/components/*/*.xml',
        'todo_list/static/src/components/*/*.scss',
    #     'todo_list/static/components/custom_todo_list/todo_list.xml',
    #     'todo_list/static/components/custom_todo_list/todo_list.scss'
        ]
    }
}

