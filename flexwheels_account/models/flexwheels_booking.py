from odoo import models, Command

class flexwheelsBooking(models.Model):
    _inherit = "flexwheels.booking"
    
    def action_done(self):
        self.env['account.move'].create(
            {
                "partner_id": self.customer_id.id,
                "move_type": "out_invoice",
                "invoice_line_ids": [Command.create({"name": self.car_id.name, "quantity": (self.drop_information - self.booking_information).days, "price_unit": self.price}),
                                     Command.create({"name": "Deposit", "quantity": 1, "price_unit": -self.car_id.deposit_amount})]
            }
        )
        return super().action_done()
