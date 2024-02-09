from odoo import fields, models
from dateutil.relativedelta import relativedelta

class flexwheelsCustomer(models.Model):
    _name = "flexwheels.booking"
    _description = "Flexwheels Booking"
    # _inherit = ['mail.thread', 'mail.activity.mixin']

    customer_id=fields.Integer()
    vehicle_id=fields.Integer()
    pickup_location=fields.Selection(
        string='Pickup Location',
        selection=[('ahmedabad', 'Ahmedabad'), ('gandhinagar', 'Gandhinagar'), ('vadodara', 'Vadodara'), ('surat', 'Surat'), ('rajkot', 'Rajkot')],
        required=True,
        tracking=True
    )
    pickup_information=fields.Datetime(required=True)
    drop_information=fields.Datetime(required=True)
    amount=fields.Float(required=True, readonly=True)
