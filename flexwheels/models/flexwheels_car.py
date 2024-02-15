from odoo import api, fields, models
from dateutil.relativedelta import relativedelta

class flexwheelsCar(models.Model):
    _name = "flexwheels.car"
    _description = "Flexwheels Car"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    brand=fields.Many2one('flexwheels.car.brand', string='Brand', required=True)
    name=fields.Char(required=True)
    type_of_vehicle=fields.Many2one('flexwheels.car.type', string='Type of Vehicle')
    price_per_km=fields.Float('flexwheels.car.type', related='type_of_vehicle.price_per_km')
    year_of_manufacturing= fields.Integer(required=True)
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
    seating_capacity=fields.Integer(required=True)
    price=fields.Float(required=True, string="Price/day", readonly=True, compute='_compute_price')
    active=fields.Boolean(default=True)
    additional_features=fields.Text()
    terms_and_conditions=fields.Text(required=True, readonly=True, default="Drive safe...")
    tag_ids=fields.Many2many("flexwheels.car.tag")
    booking_ids=fields.One2many('flexwheels.booking', 'car_id', string=' ')
    
    @api.depends('price', 'year_of_manufacturing')
    def _compute_deposit_amount(self):
        for record in self:
            record.deposit_amount=record.price*2.5
    
    @api.depends('type_of_vehicle')
    def _compute_price(self):
        for record in self:
            record.price=record.price_per_km*250
