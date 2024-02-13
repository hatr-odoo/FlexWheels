from odoo import fields, models
from dateutil.relativedelta import relativedelta

class flexwheelsCar(models.Model):
    _name = "flexwheels.car"
    _description = "Flexwheels Car"
    # _inherit = ['mail.thread', 'mail.activity.mixin']

    brand=fields.Selection(
        string="Brand",
        selection=[
                ('maruti suzuki', 'Maruti Suzuki'),
                ('hyundai', 'Hyundai'),
                ('tata', 'Tata'),
                ('mahindra', 'Mahindra'),
                ('kia', 'Kia'),
                ('honda', 'Honda'),
                ('toyota', 'Toyota'),
                ('ford', 'Ford'),
                ('volkswagen', 'Volkswagen'),
                ('renault', 'Renault'),
                ('mg', 'MG'),
                ('nissan', 'Nissan'),
                ('skoda', 'Skoda'),
                ('bmw', 'BMW'),
                ('mercedes-benz', 'Mercedes-Benz'),
                ('audi', 'Audi'),
                ('jeep', 'Jeep'),
                ('volvo', 'Volvo'),
                ('land rover', 'Land Rover'),
                ('jaguar', 'Jaguar'),
                ('fiat', 'Fiat'),
                ('mitsubishi', 'Mitsubishi'),
                ('isuzu', 'Isuzu'),
                ('porsche', 'Porsche'),
                ('rolls-royce', 'Rolls-Royce'),
                ('lamborghini', 'Lamborghini'),
                ('maserati', 'Maserati'),
                ('bentley', 'Bentley'),
                ('ferrari', 'Ferrari'),
                ('other', 'Other')
                ],
        required=True
    )
    name=fields.Char(required=True)
    type_of_vehicle=fields.Selection(
        required=True,
        string="Type",
        selection=[
                    ('hatchback', 'Hatchback'),
                    ('sedan', 'Sedan'),
                    ('suv', 'SUV'),
                    ('mpv', 'MPV'),
                    ('crossover', 'Crossover'),
                    ('coupe', 'Coupe'),
                    ('convertible', 'Convertible')
                ]
    )
    year_of_manufacturing= fields.Integer(required=True)
    deposit_amount=fields.Float(required=True)
    variant=fields.Char(required=True)
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

    )
    transmission=fields.Selection(
        string='Transmission',
        selection=[('manual', 'Manual'), ('automatic', 'Automatic')],
        required=True,

    )
    seating_capacity=fields.Integer(required=True)
    price=fields.Float(required=True)
    active=fields.Boolean(default=True)
    location=fields.Selection(
        string='Location',
        selection=[('ahmedabad', 'Ahmedabad'), 
                   ('gandhinagar', 'Gandhinagar'), 
                   ('vadodara', 'Vadodara'), 
                   ('surat', 'Surat'), 
                   ('rajkot', 'Rajkot')],
        required=True,

    )
    additional_features=fields.Text()
    terms_and_conditions=fields.Text(required=True, readonly=True, default="Drive safe...")
    tag_ids=fields.Many2many("flexwheels.car.tag")
