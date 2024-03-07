import datetime
import re
from odoo import api, fields, models
from dateutil.relativedelta import relativedelta

from odoo.exceptions import ValidationError

class flexwheelsCustomer(models.Model):
    _name = "flexwheels.customer"
    _description = "Flexwheels Customer"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name=fields.Char(required=True)
    license=fields.Char(required=True)
    address=fields.Text(required=True)
    city=fields.Char(required=True)
    image = fields.Binary(required=True)
    license_image = fields.Binary(required=True)
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
    contact_number=fields.Char(required=True)
    birth_date=fields.Date(required=True)
    occupation=fields.Char(required=True)
    emergency_contact_number=fields.Char(required=True)
    
    _sql_constraints = [('license_unique', 'unique(license)', 'Customer with same license number already exists.')]
    
    @api.constrains('contact_number', 'emergency_contact_number')
    def _check_contact_number(self):
        for record in self:
            if not len(record.contact_number) == 10:
                raise ValidationError('Invalid Phone number.')
            elif not len(record.emergency_contact_number) ==10:
                raise ValidationError('Invalid Emergency contact number')
            
    @api.constrains('license')
    def _check_license(self):
        license_number_pattern = r'^(([A-Z]{2}[0-9]{2})( )|([A-Z]{2}-[0-9]{2}))((19|20)[0-9][0-9])[0-9]{7}$'
        for record in self:
            if re.match(license_number_pattern, record.license) is None:
                raise ValidationError('Invalid driving license number. Eg. HR-0619850034761')
    
    @api.constrains('birth_date')
    def _check_birth_date(self):
        for record in self:
            today = fields.date.today()
            age = today.year - record.birth_date.year - ((today.month, today.day) < (record.birth_date.month, record.birth_date.day))
            
            if age<18:
                raise ValidationError('Age must be above 18 years')
