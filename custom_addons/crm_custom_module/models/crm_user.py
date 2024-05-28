from odoo import models, fields, api
class CRMUser(models.Model):
    _name = 'crm.user'
    name=fields.Char(string='Name')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')


