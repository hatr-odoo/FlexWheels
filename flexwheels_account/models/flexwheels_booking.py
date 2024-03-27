from odoo import models, Command

class flexwheelsbooking(models.Model):
    
    _inherit = "flexwheels.booking.wizard"
    
    def action_done(self):
        super().action_done()
        
        if not self.bookings.customer_id.partner_id:
            partner_id = self.env['res.partner'].create({
                'name': self.bookings.customer_id.name,
                'is_company': False,
                'street':self.bookings.customer_id.address,
                'phone': self.bookings.customer_id.contact_number,
                'function': self.bookings.customer_id.occupation
            })
            self.bookings.customer_id.partner_id = partner_id.id
        
        self.bookings.env['account.move'].create(
            {
                "partner_id": self.bookings.customer_id.partner_id.id,
                "move_type": "out_invoice",
                "invoice_line_ids": [Command.create({"name": self.bookings.car_id.name, "quantity": (self.bookings.drop_information - self.bookings.pickup_information).total_seconds() / 3600, "price_unit": self.bookings.price}),
                                    Command.create({"name": "Trip Protection Fee", "quantity": 1, "price_unit": 419}),
                                    Command.create({"name": "Convenience Fee", "quantity": 1, "price_unit": 99}),
                                    Command.create({"name": "Refundable Deposit", "quantity": 1, "price_unit": -self.bookings.deposit_amount})]
            }
        )
        return True
