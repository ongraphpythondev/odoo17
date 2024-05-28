from odoo import models, fields

class Order(models.Model):
    _name = "ecommerce.order"
    _description = "This is an order"

    customer = fields.Many2one('ecommerce.customer', string="Customer")
    total_amount = fields.Float(string="Total Amount", required=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('delivered', 'Delivered')
    ], string="Status", default='draft')
    date = fields.Datetime(default=fields.Datetime.now)
    order_line = fields.One2many("ecommerce.orderline", "order", string="Order Lines", ondelete='cascade')


class OrderLine(models.Model):
      _name="ecommerce.orderline"
      _description="this is an order line model"
      product = fields.Many2one("ecommerce.product", string="Product", required=True)
      quantity = fields.Integer(string="Quantity", default=0)
      price = fields.Float(string="Price", required=True)
      order=fields.Many2one('ecommerce.order',string="Order")