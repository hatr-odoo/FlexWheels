{
    'name': "FlexWheels",
    'version': '1.0',
    'depends': ['base', 'mail'],
    'author': "hatr-odoo",
    'category': 'FlexWheels',
    'description': """
    Description text
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/car_views.xml',
        'views/customer_views.xml',
        'views/booking_views.xml',
        'views/invoice_views.xml',
        'views/flexwheels_menus.xml',
    ],
    'application': True,
    'installable': True,
    'license': 'OEEL-1'
}
