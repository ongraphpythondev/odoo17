from odoo import models, fields, api


class Cart(models.Model):
    _name = "ecommerce.cart"
    _description = "Cart Model"

    user = fields.Many2one("ecommerce.customer", string="Customer")
    cart_line = fields.One2many("ecommerce.cartline", "cart", string="Cart Lines", ondelete='cascade')

    def delete_one2many(self):
        print("working*********************88888")
        for record in self:
            if record.cart_line:
                record.cart_line=[(5,0,0)]  
                return{
                        'effect':{
                        'fadeout': 'slow',
                        'type':'rainbow_man',
                        'message': 'Record has been deleted successfully'
                        }
                    }
class CartLine(models.Model):
    _name = "ecommerce.cartline"
    _description = "Cart Line Model"

    product = fields.Many2one("ecommerce.product", string="Product", required=True)
    quantity = fields.Integer(string="Quantity", default=1)
    cart = fields.Many2one("ecommerce.cart", string="Cart")