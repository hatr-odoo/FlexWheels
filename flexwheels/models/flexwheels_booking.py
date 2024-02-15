from odoo import api, fields, models
from odoo.exceptions import UserError

class flexwheelsCustomer(models.Model):
    _name = "flexwheels.booking"
    _description = "Flexwheels Booking"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name=fields.Integer()
    customer_id=fields.Many2one('flexwheels.customer', string="Customer", required=True)
    car_id=fields.Many2one('flexwheels.car', string="Car", required=True)
    price=fields.Float('flexwheels.car', related='car_id.price')
    booking_information=fields.Date(required=True, default=fields.Date.today(), readonly=True)
    drop_information=fields.Date(required=True)
    billing_amount=fields.Float(required=True, compute='_compute_billing_amount')
    state=fields.Selection(
        string="Status",
        selection=[('draft', 'Draft'), 
                   ('confirm', 'Confirm'), 
                   ('cancelled', 'Cancelled'), 
                   ('ongoing', 'Ongoing'), 
                   ('done', 'Done')],
        default='draft'
    )

    @api.depends('price', 'drop_information', 'booking_information')
    def _compute_billing_amount(self):
        for record in self:
            if record.booking_information and record.drop_information:
                date_difference = (record.drop_information - record.booking_information).days
                if date_difference >= 0:
                    record.billing_amount = record.price * (date_difference+1)
                else:
                    record.billing_amount = 0
            else:
                record.billing_amount = 0
    
    @api.onchange('car_id')
    def _onchange_car(self):
        for record in self:
            record.car_id.is_available=False
                   
    def action_confirm(self):
        for record in self:
            if not record.state=='cancelled':
                record.state='confirm'
                return True
            raise UserError('Cancelled bookings cannot be confirmed.')
    
    def action_cancel(self):
        for record in self:
            if not record.state=='confirm':
                record.state='cancelled'
                return True
            raise UserError('Confirmed bookings cannot be cancelled.')         
