from odoo import models, fields

class inheritResUsers(models.Model):
    _inherit = "res.users"
    
    booking_ids = fields.One2many('flexwheels.booking', 'salesperson_id', domain=[("state", "in", ["confirm", "ongoing", "done"])])
