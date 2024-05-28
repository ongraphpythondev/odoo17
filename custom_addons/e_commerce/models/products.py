from odoo import models, fields, api
import base64
import os


class Products(models.Model):
    _name = "ecommerce.product"
    _description = "Product Model"

    name = fields.Char(string="product_name", required=True)
    description = fields.Char(string="Description")
    price = fields.Float(string="Price", required=True)
    quantity = fields.Integer(string="Quantity", default=0)
    category = fields.Many2one("ecommerce.category", string="Category")
    image = fields.Binary(string="Product Image")
    sequence = fields. Integer (string="Seq.")
    status = fields. Selection ([('active', 'Active'), ('deactive', 'Deactive')], string="Status", readonly=True, default="active")

    def new_fun(self):
        print("workin object button ^^^^^^^^^^^^^^^^^^^")

    def change_status(self):
        for rec in self:
            if rec.status == 'active':
                rec.status = 'deactive'
                msg = 'Status is now deactive'
            else:
                rec.status = 'active'
                msg = 'Status is now active'

        return{
                'effect':{
                'fadeout': 'slow',
                'type':'rainbow_man',
                'message': msg
                 }
               }

class Category(models.Model):
    _name = "ecommerce.category"
    _description = "product category"

    name = fields.Char(string="Category Name", required=True)
    description = fields.Text(string="Category Description")
