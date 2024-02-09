from odoo import fields, models
from dateutil.relativedelta import relativedelta

class flexwheelsInvoice(models.Model):
    _name = "flexwheels.invoice"
    _description = "Flexwheels Invoice"
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    
    invoice_number=fields.Integer(required=True)
    customer_id=fields.Integer(required=True)
    vehicle_id=fields.Integer(required=True)
    customer_name=fields.Char(required=True)
    model=fields.Char(required=True)
    period_of_service=fields.Integer(required=True)
    amount=fields.Float(required=True, readonly=True)
