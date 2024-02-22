from odoo import api, fields, models
import re

from odoo.exceptions import ValidationError

class flexwheelsCar(models.Model):
    _name = "flexwheels.car"
    _description = "Flexwheels Car"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    brand=fields.Many2one('flexwheels.car.brand', string='Brand', required=True)
    name=fields.Char(required=True)
    image=fields.Binary(required=True, copy=False)
    car_type_id=fields.Many2one('flexwheels.car.type', string='Type of Vehicle')
    price = fields.Float(required=True)
    years_tuple=[(str(year), str(year)) for year in range(fields.Date.today().year, 1884, -1)]
    year_of_manufacturing = fields.Selection(
        years_tuple, 
        string='Year of Manufacturing', 
        required=True
    )
    variant=fields.Char(required=True)
    is_available=fields.Boolean(default=True)
    color=fields.Selection(
        string='Color',
        selection=[('white', 'White'),
                   ('silver', 'Silver'),
                   ('black', 'Black'),
                   ('grey', 'Grey'),
                   ('blue', 'Blue'),
                   ('red', 'Red'),
                   ('brown', 'Brown'),
                   ('beige', 'Beige'),
                   ('yellow', 'Yellow'),
                   ('green', 'Green'), 
                   ('others', 'Others')],
        required=True,
        default='white',
        tracking=True
    )
    registration_number=fields.Char(required=True, copy=False)
    chassis_number=fields.Char(required=True, copy=False)
    registration_book_image=fields.Binary(required=True, copy=False)
    mileage=fields.Float()
    fuel_type=fields.Selection(
        string='Fuel Type',
        selection=[('petrol', 'Petrol'),
                   ('diesel', 'Diesel'),
                   ('cng', 'CNG'),
                   ('lpg', 'LPG'),
                   ('electric', 'Electric'),
                   ('hybrid', 'Hybrid')],
        required=True,
        tracking=True
    )
    transmission=fields.Selection(
        string='Transmission',
        selection=[('manual', 'Manual'), ('automatic', 'Automatic')],
        required=True,
        tracking=True
    )
    seating_capacity=fields.Integer(required=True, default=5)
    active=fields.Boolean(default=True)
    additional_features=fields.Text(copy=False)
    tag_ids=fields.Many2many("flexwheels.car.tag")
    booking_ids=fields.One2many('flexwheels.booking', 'car_id', string=' ', copy=False)
    done_booking_ids=fields.One2many('flexwheels.booking', 'car_id', compute='_compute_done_booking_id', string=" ", copy=False)
    
    _sql_constraints=[('check_seating_capacity', 'CHECK(seating_capacity>1)', 'Seating capacity must be atleast 2'),
                      ('registration_number_unique', 'unique(registration_number)', 'Car with same registration number already exists.'),
                      ('chassis_number_unique', 'unique(chassis_number)', 'Car with same chassis number already exists.')]
    
    @api.depends('booking_ids')
    def _compute_done_booking_id(self):
        for record in self:
            record.done_booking_ids=record.booking_ids.filtered(
                lambda booking: booking.state=='done'
            )
    
    @api.constrains('registration_number')
    def _check_registration_number(self):
        for record in self:
            pattern = r'^[A-Z]{2}[0-9]{1,2}[A-Z]{1,2}[0-9]{1,4}$'
            if not re.match(pattern, record.registration_number) is not None:
                raise ValidationError('Invalid registration number. Ex: MH12AB1234')
        
    @api.constrains('price')
    def _check_registration_number(self):
        for record in self:
            if not record.price>0:
                raise ValidationError('Price should be strictly positive.')
        
    @api.constrains('chassis_number')
    def _check_chassis_number(self):
        for record in self:
            if not len(record.chassis_number)==17:
                raise ValidationError('Invalid chassis number. Chassis number must consist of 17 alphanumeric characters. Example: ABZ12345CD6789012')
