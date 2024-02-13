from odoo import api, fields, models

class flexwheelsCustomer(models.Model):
    _name = "flexwheels.booking"
    _description = "Flexwheels Booking"
    # _inherit = ['mail.thread', 'mail.activity.mixin']

    customer=fields.Many2one('flexwheels.customer', string="Customer", required=True)
    car=fields.Many2one('flexwheels.car', string="Car", required=True)
    booking_information=fields.Date(required=True, default=fields.Date.today())
    pickup_location=fields.Selection(
        string='Pickup Location',
        selection=[('ahmedabad', 'Ahmedabad'), ('gandhinagar', 'Gandhinagar'), ('vadodara', 'Vadodara'), ('surat', 'Surat'), ('rajkot', 'Rajkot')],
        required=True,
        tracking=True
    )
    pickup_information=fields.Date(required=True)
    drop_information=fields.Date(required=True)
    amount=fields.Float(required=True)
