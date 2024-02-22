from odoo import models, Command

class flexwheelsBooking(models.Model):
    _inherit = "flexwheels.booking"
    
    def action_done(self):
        self.env['account.move'].create(
            {
                "partner_id": self.customer_id.id,
                "move_type": "out_invoice",
                "invoice_line_ids": [Command.create({"name": self.car_id.name, "quantity": (self.drop_information - self.pickup_information).total_seconds() / 3600, "price_unit": self.price}),
                                     Command.create({"name": "Trip Protection Fee", "quantity": 1, "price_unit": 419}),
                                     Command.create({"name": "Convenience Fee", "quantity": 1, "price_unit": 99}),
                                     Command.create({"name": "Refundable Deposit", "quantity": 1, "price_unit": -self.deposit_amount})]
            }
        )
        return super().action_done()
