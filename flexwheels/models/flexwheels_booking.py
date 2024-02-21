from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

class flexwheelsBooking(models.Model):
    _name = "flexwheels.booking"
    _description = "Flexwheels Booking"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    customer_id=fields.Many2one('flexwheels.customer', string="Customer", required=True)
    salesperson_id=fields.Many2one('res.users', default= lambda self: self.env.user, tracking=True)
    car_id=fields.Many2one('flexwheels.car', string="Car", required=True)
    price=fields.Float('flexwheels.car', related='car_id.price')
    booking_information=fields.Date(required=True, default=fields.Date.today(), readonly=True)
    pickup_information=fields.Date(required=True, default=fields.Date.today(), readonly=True)
    drop_information=fields.Date(required=True)
    seq_name = fields.Char(string='Booking Reference', required=True, readonly=True, copy=False, default= lambda self: ('New'))
    state=fields.Selection(
        string="Status",
        selection=[('draft', 'Draft'), 
                   ('confirm', 'Confirm'), 
                   ('cancelled', 'Cancelled'), 
                   ('ongoing', 'Ongoing'), 
                   ('done', 'Done')],
        default='draft'
    )
                   
    def action_confirm(self):
        for record in self:
            if record.state=='draft':
                record.state='confirm'
                return True
            raise UserError('Confirmation not possible.')
    
    def action_ongoing(self):
        for record in self:
            if record.state=='confirm':
                record.state='ongoing'
                record.car_id.is_available=False
                return True
            raise UserError('Ongoing not possible.')
    
    def action_done(self):
        for record in self:
            if record.state=='ongoing':
                record.state='done'
                record.car_id.is_available=True
                return True
            raise UserError('Done not possible.')
    
    def action_cancel(self):
        for record in self:
            if record.state=='draft' and record.state=='confirm':
                record.state='cancelled'
                return True
            raise UserError('Cancellation not possible at this stage')
        
    @api.constrains('pickup_information')
    def _check_drop_information(self):
        for record in self:
            if record.drop_information < record.pickup_information:
                raise ValidationError("The drop date cannot be before pickup date")
        
    @api.model
    def create(self, vals):
        if not 'seq_name' in vals:
            vals['seq_name'] = self.env['ir.sequence'].next_by_code('flexwheels.booking') or 'New'
        return super().create(vals)

    @api.model
    def write(self, vals):
        if 'car_id' in vals:
            old_car_id = self.car_id.id
            
            old_car = self.env['flexwheels.car'].browse(old_car_id)
            old_car.is_available = True

        return super().write(vals)
