# -*- coding: utf-8 -*-
{
    'name': "Employee",

    'summary': """
        Employee Details""",

    'description': """
        Employee Details
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        "data/tags.xml",
        'views/employee_views.xml',
        'views/employee_category_views.xml',
    ]
}
