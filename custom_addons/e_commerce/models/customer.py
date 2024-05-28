# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Customers(models.Model):
    _name = 'ecommerce.customer'
    _inherits= {'res.partner': 'customuuser_id'}
    _inherit=['mail.thread','mail.activity.mixin']
    _description = 'this is for e-commerce customer'
    name=fields.Char(string='Name',track_visibility='always')
    customuuser_id= fields.Many2one('res.partner', string='Related Partner', required=True, ondelete='cascade')
    password = fields.Char(string='Password')
    
    
    
    
    @api.constrains('password')
    def val_password(self):
            for rec in self:
                if rec.password and not rec.password.isdigit():
                    raise ValidationError("Password must contain only numbers.")
                if rec.password and len(rec.password) != 4:
                    raise ValidationError("Password must be exactly 4 digits long.")

    # @api.multi
    # def unlink(self):
    #     for customer in self:
    #         print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^6")
    #         if customer.customuuser_id:
    #             customer.customuuser_id.unlink()
    #     return super(Customers, self).unlink() 
    
    
    # def action_send_mail(self):
    #     template=self.env.ref('e_commerce.')
    