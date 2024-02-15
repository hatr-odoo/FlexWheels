from odoo import fields, models

class flexwheelsCarBrand(models.Model):
    _name = "flexwheels.car.brand"
    _description = "Flexwheels Car Brand Model"
    
    name = fields.Char(required=True)
