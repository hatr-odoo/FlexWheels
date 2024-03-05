{
    'name': "FlexWheels",
    'version': '1.0',
    'depends': ['base', 'mail'],
    'author': "hatr-odoo",
    'category': 'FlexWheels/Flexwheels',
    'description': """
    Description text
    """,
    'data': [
        'security/ir.model.access.csv',
        'data/booking_sequence.xml',
        'wizard/flexwheels_booking_wizard.xml',
        'views/flexwheels_car_views.xml',
        'views/flexwheels_customer_views.xml',
        'views/flexwheels_booking_views.xml',
        'views/flexwheels_car_brand_views.xml',
        'views/flexwheels_car_type_views.xml',
        'views/flexwheels_res_users_views.xml',
        'views/flexwheels_tag_views.xml',
        'views/flexwheels_menus.xml',
    ],
    'application': True,
    'installable': True,
    'license': 'OEEL-1'
}
