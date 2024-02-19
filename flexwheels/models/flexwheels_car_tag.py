from random import randint
from odoo import fields, models

class flexwheelsCarTag(models.Model):
    _name = "flexwheels.car.tag"
    _description = "Flexwheels Car Tag Model"

    def _get_default_color(self):
        return randint(1, 11)
    
    name = fields.Char(required=True)
    color = fields.Integer(string="Color", default=_get_default_color)
    _sql_constraints=[('name_unique', 'unique(name)', 'Tag with given name already exists.')]
