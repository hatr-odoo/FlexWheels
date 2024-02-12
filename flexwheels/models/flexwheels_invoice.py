from odoo import fields, models
from dateutil.relativedelta import relativedelta

class flexwheelsInvoice(models.Model):
    _name = "flexwheels.invoice"
    _description = "Flexwheels Invoice"
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    
    invoice_number=fields.Integer(required=True, default="11")
    customer=fields.Many2one('flexwheels.customer', string="Customer", required=True)
    car=fields.Many2one('flexwheels.car', string="Car", required=True)
    period_of_service=fields.Integer(required=True)
    amount=fields.Float(required=True)
