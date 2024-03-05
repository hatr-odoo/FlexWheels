from odoo import api, models, fields
from odoo.exceptions import UserError, ValidationError

class flexwheelsBookingWizard(models.Model):
    _name = "flexwheels.booking.wizard"
    
    odometer_reading = fields.Float(required=True)
    
    bookings = fields.Many2one('flexwheels.booking', compute = "_compute_bookings")
    
    api.depends()
    def _compute_bookings(self):
        for record in self:
            record.bookings = self.env['flexwheels.booking'].browse(self.env.context.get('active_ids', []))
    
    #method for making booking done
    def action_done(self):
        if self.bookings.car_id.kms_driven >= self.odometer_reading:
            raise ValidationError('New reading must be more than old reading')
        self.bookings.car_id.kms_driven = self.odometer_reading
            
        if self.bookings.state=='ongoing':
            self.bookings.state='done'
            self.bookings.car_id.is_available=True
            return True
        raise UserError('Done not possible.')
