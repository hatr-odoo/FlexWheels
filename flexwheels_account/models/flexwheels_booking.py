from odoo import models, Command

class flexwheelsbooking(models.Model):
    
    _inherit = "flexwheels.booking.wizard"
    
    def action_done(self):
        super().action_done()
        self.bookings.env['account.move'].create(
            {
                "partner_id": self.bookings.customer_id.id,
                "move_type": "out_invoice",
                "invoice_line_ids": [Command.create({"name": self.bookings.car_id.name, "quantity": (self.bookings.drop_information - self.bookings.pickup_information).total_seconds() / 3600, "price_unit": self.bookings.price}),
                                    Command.create({"name": "Trip Protection Fee", "quantity": 1, "price_unit": 419}),
                                    Command.create({"name": "Convenience Fee", "quantity": 1, "price_unit": 99}),
                                    Command.create({"name": "Refundable Deposit", "quantity": 1, "price_unit": -self.bookings.deposit_amount})]
            }
        )
        return True
