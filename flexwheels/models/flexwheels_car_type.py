from odoo import api, fields, models

class flexwheelsCarType(models.Model):
    _name = "flexwheels.car.type"
    _description = "Flexwheels Car Type Model"
    
    name = fields.Char(required=True)
    booking_ids = fields.One2many('flexwheels.booking', 'car_type_id')
    booking_count = fields.Integer(compute='_compute_booking_count')
    
    _sql_constraints=[('name_unique', 'unique(name)', 'The given type of car already exists.')]
    
    #method to compute count of bookings
    @api.depends('booking_ids')
    def _compute_booking_count(self):
        for record in self:
            record.booking_count=len(record.booking_ids)
