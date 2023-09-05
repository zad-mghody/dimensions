# -*- coding: utf-8 -*-
{
    'name': "Dimension",
    'summary': """My third task about sales module """,
    'description': """
        Long description of module's purpose
    """,
    'author': "Mohannad Ghody",
    'website': "https://www.yourcompany.com",
    'category': 'Sales/CRM',
    'version': '0.1',
    'sequence': 2,
    'depends': ['base', 'product', 'sale', 'stock', 'mrp', 'account', 'point_of_sale', 'sale_stock', 'stock_account'],
    'data': [
        'views/product_template_inherit_views.xml',
        'views/sale_order_inherit_views.xml',
        'views/inventory_inherit_views.xml',
        'views/invoice_inherit_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
