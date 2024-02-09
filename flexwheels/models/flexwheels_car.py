from odoo import fields, models
from dateutil.relativedelta import relativedelta

class flexwheelsCar(models.Model):
    _name = "flexwheels.car"
    _description = "Flexwheels Car"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    brand=fields.Char(required=True, tracking=True)
    model=fields.Char(required=True, tracking=True)
    year_of_manufacturing= fields.Integer(required=True)
    deposit_amount=fields.Float(required=True)
    variant=fields.Char(required=True)
    color=fields.Selection(
        string='Color',
        selection=[('white', 'White'),('silver', 'Silver'),('black', 'Black'),('grey', 'Grey'),('blue', 'Blue'),('red', 'Red'),('brown', 'Brown'),('beige', 'Beige'),('yellow', 'Yellow'),('green', 'Green'), ('others', 'Others')],
        required=True,
        default='white',
        tracking=True
    )
    license_plate_number=fields.Char(required=True)
    mileage=fields.Float()
    fuel_type=fields.Selection(
        string='Fuel Type',
        selection=[('petrol', 'Petrol'),('diesel', 'Diesel'),('cng', 'CNG'),('lpg', 'LPG'),('electric', 'Electric'),('hybrid', 'Hybrid')],
        required=True,
        tracking=True
    )
    transmission=fields.Selection(
        string='Transmission',
        selection=[('manual', 'Manual'), ('automatic', 'Automatic')],
        required=True,
        tracking=True
    )
    seating_capacity=fields.Integer(required=True, tracking=True)
    price=fields.Float(required=True)
    active=fields.Boolean(default=True, tracking=True)
    location=fields.Selection(
        string='Location',
        selection=[('ahmedabad', 'Ahmedabad'), ('gandhinagar', 'Gandhinagar'), ('vadodara', 'Vadodara'), ('surat', 'Surat'), ('rajkot', 'Rajkot')],
        required=True,
        tracking=True
    )
    additional_features=fields.Text()
    terms_and_conditions=fields.Text(required=True, readonly=True)
