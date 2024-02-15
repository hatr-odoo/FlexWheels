from odoo import fields, models

class flexwheelsCarType(models.Model):
    _name = "flexwheels.car.type"
    _description = "Flexwheels Car Type Model"
    
    name = fields.Char(required=True)
    price_per_km = fields.Float(required=True, string="Price per km")
