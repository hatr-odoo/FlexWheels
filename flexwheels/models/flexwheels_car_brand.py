from odoo import fields, models

class flexwheelsCarBrand(models.Model):
    _name = "flexwheels.car.brand"
    _description = "Flexwheels Car Brand Model"
    
    name = fields.Char(required=True)
    brand_logo = fields.Binary(required=True)
    _sql_constraints=[('name_unique', 'unique(name)', 'Brand with this name already exists.')]
