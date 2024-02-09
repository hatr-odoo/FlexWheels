from odoo import fields, models
from dateutil.relativedelta import relativedelta

class flexwheelsCustomer(models.Model):
    _name = "flexwheels.customer"
    _description = "Flexwheels Customer"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name=fields.Char(required=True)
    license=fields.Char(required=True)
    address=fields.Text(required=True)
    city=fields.Char(required=True)
    state=fields.Char(required=True)
    contact_number=fields.Integer(required=True)
    birth_date=fields.Date(required=True)
    occupation=fields.Char(required=True)
    emergency_contact_number=fields.Integer(required=True)
