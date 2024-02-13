{
    'name': "FlexWheels",
    'version': '1.0',
    'depends': ['base'],
    'author': "hatr-odoo",
    'category': 'FlexWheels',
    'description': """
    Description text
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/flexwheels_tag_views.xml',
        'views/flexwheels_car_views.xml',
        'views/flexwheels_customer_views.xml',
        'views/flexwheels_booking_views.xml',
        'views/flexwheels_invoice_views.xml',
        'views/flexwheels_menus.xml',
    ],
    'application': True,
    'installable': True,
    'license': 'OEEL-1'
}
