from odoo import fields, models
from dateutil.relativedelta import relativedelta

class flexwheelsCustomer(models.Model):
    _name = "flexwheels.customer"
    _description = "Flexwheels Customer"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name=fields.Char(required=True)
    license=fields.Char(required=True)
    address=fields.Text(required=True)
    city=fields.Char(required=True)
    state=fields.Selection(required=True,
                           string="Select State",
                           selection= [
                                        ('andhra pradesh', 'Andhra Pradesh'),
                                        ('arunachal pradesh', 'Arunachal Pradesh'),
                                        ('assam', 'Assam'),
                                        ('bihar', 'Bihar'),
                                        ('chhattisgarh', 'Chhattisgarh'),
                                        ('goa', 'Goa'),
                                        ('gujarat', 'Gujarat'),
                                        ('haryana', 'Haryana'),
                                        ('himachal pradesh', 'Himachal Pradesh'),
                                        ('jammu and kashmir', 'Jammu and Kashmir'),
                                        ('jharkhand', 'Jharkhand'),
                                        ('karnataka', 'Karnataka'),
                                        ('kerala', 'Kerala'),
                                        ('madhya pradesh', 'Madhya Pradesh'),
                                        ('maharashtra', 'Maharashtra'),
                                        ('manipur', 'Manipur'),
                                        ('meghalaya', 'Meghalaya'),
                                        ('mizoram', 'Mizoram'),
                                        ('nagaland', 'Nagaland'),
                                        ('odisha', 'Odisha'),
                                        ('punjab', 'Punjab'),
                                        ('rajasthan', 'Rajasthan'),
                                        ('sikkim', 'Sikkim'),
                                        ('tamil nadu', 'Tamil Nadu'),
                                        ('telangana', 'Telangana'),
                                        ('tripura', 'Tripura'),
                                        ('uttar pradesh', 'Uttar Pradesh'),
                                        ('uttarakhand', 'Uttarakhand'),
                                        ('west bengal', 'West Bengal'),
                                        ('andaman and nicobar islands', 'Andaman and Nicobar Islands'),
                                        ('chandigarh', 'Chandigarh'),
                                        ('dadra and nagar haveli and daman and diu', 'Dadra and Nagar Haveli and Daman and Diu'),
                                        ('delhi', 'Delhi'),
                                        ('lakshadweep', 'Lakshadweep'),
                                        ('puducherry', 'Puducherry')
                                ]
)
    contact_number=fields.Integer(required=True)
    birth_date=fields.Date(required=True)
    occupation=fields.Char(required=True)
    emergency_contact_number=fields.Integer(required=True)
