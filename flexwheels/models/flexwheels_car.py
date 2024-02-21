from odoo import api, fields, models
import re

from odoo.exceptions import ValidationError

class flexwheelsCar(models.Model):
    _name = "flexwheels.car"
    _description = "Flexwheels Car"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    brand=fields.Many2one('flexwheels.car.brand', string='Brand', required=True)
    name=fields.Char(required=True)
    type_of_vehicle=fields.Many2one('flexwheels.car.type', string='Type of Vehicle')
    price_per_km=fields.Float('flexwheels.car.type', related='type_of_vehicle.price_per_km')
    year_of_manufacturing= fields.Integer(required=True, default=fields.Date.today().year)
    deposit_amount=fields.Float(required=True, compute='_compute_deposit_amount')
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
    license_plate_number=fields.Char(required=True)
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
    price=fields.Float(required=True, string="Price/day", readonly=True, compute='_compute_price')
    active=fields.Boolean(default=True)
    additional_features=fields.Text()
    terms_and_conditions=fields.Text(required=True, readonly=True, default="Drive safe...")
    tag_ids=fields.Many2many("flexwheels.car.tag")
    booking_ids=fields.One2many('flexwheels.booking', 'car_id', string=' ')
    done_booking_ids=fields.One2many('flexwheels.booking', 'car_id', compute='_compute_done_booking_id', string=" ")
    
    _sql_constraints=[('check_seating_capacity', 'CHECK(seating_capacity>1)', 'Seating capacity must be atleast 2'),
                      ('license_plate_number_unique', 'unique(license_plate_number)', 'Car with same license plate number already exists.')]
    
    @api.depends('booking_ids')
    def _compute_done_booking_id(self):
        for record in self:
            record.done_booking_ids=record.booking_ids.filtered(
                lambda booking: booking.state=='done'
            )
    
    @api.depends('price', 'year_of_manufacturing')
    def _compute_deposit_amount(self):
        for record in self:
            record.deposit_amount=record.price*2.5
    
    @api.depends('type_of_vehicle')
    def _compute_price(self):
        for record in self:
            record.price=record.price_per_km*250
    
    @api.constrains('license_plate_number')
    def _check_license_plate_number(self):
        for record in self:
            pattern = r'^[A-Z]{2}[0-9]{1,2}[A-Z]{1,2}[0-9]{4}$'
            if not re.match(pattern, record.license_plate_number) is not None:
                raise ValidationError('Invalid license plate number. Ex: MH12AB1234')
            
    @api.constrains('year_of_manufacturing')
    def _check_seating_capacity(self):
        for record in self:
            if record.year_of_manufacturing>(fields.Date.today().year):
                raise ValidationError('Year of manufacturing can not be in the future')
            elif record.year_of_manufacturing<1884:
                raise ValidationError('Ancient car detected. Keep the car in modern times.')
