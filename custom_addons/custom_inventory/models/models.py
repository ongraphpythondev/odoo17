from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
   
class InventoryEntry(models.Model):
    _name = 'custom_inventory.entry'
    _description = 'Inventory Entry'

    serial_number = fields.Char(string='Serial Number', readonly=True)
    date = fields.Date(string='Date', default=fields.Date.today(), readonly=True)
    supplier_id = fields.Many2one('res.partner', string='Supplier', domain=[('supplier_rank','>', 0)], required=True)
    vehicle_number = fields.Char(string='Vehicle Number', required=True)   
    
    @api.model
    def create(self, vals):
        sequence = self.env['ir.sequence'].next_by_code('custom_inventory.entry') or '/'
        vals['serial_number'] = sequence
        return super(InventoryEntry, self).create(vals)
    

class OrderProforma(models.Model):
    _name = 'order.proforma'
    _description = 'Order Proforma'

    order_number = fields.Char(string='Order Proforma Number', readonly=True, copy=False, index=True, default=lambda self:_('New'))
    date = fields.Date(string='Date', default=fields.Date.today(), required=True)
    inventory_ids = fields.One2many('assigned.stock', 'order_proforma_id', string='Assigned Inventory')
    total_inventory = fields.Integer(string='Total Inventory', compute='_compute_total_inventory')

    @api.depends('inventory_ids.quantity')
    def _compute_total_inventory(self):
        for record in self:
            record.total_inventory = sum(record.inventory_ids.mapped('quantity'))
    @api.model
    def create(self, vals):
        if vals.get('order_number', _('New')) == _('New'):
            vals['order_number'] = self.env['ir.sequence'].next_by_code('order.proforma') or '/'
        return super(OrderProforma, self).create(vals)
         
        return sequence_obj
class AssignedStock(models.Model):
    _name = 'assigned.stock'
    _description = 'Assigned Stock'

    order_proforma_id = fields.Many2one('order.proforma', string='Order Proforma', required=True, ondelete='cascade')
    inventory_id = fields.Many2one('product.product', string='Inventory', required=True)
    quantity = fields.Integer(string='Quantity', default=1)

class InboundStock(models.Model):
    _name = 'inbound.stock'
    _description = 'Inbound Stock'

    inventory_id = fields.Many2one('product.product', string='Inventory', required=True)
    quantity = fields.Integer(string='Quantity', default=1)
    date = fields.Date(string='Date', default=fields.Date.today(), required=True)
    barcode = fields.Char(string='Barcode')
    tag = fields.Char(string='Tag')
    comments = fields.Text(string='Comments')

class StockDiscrepancy(models.Model):
    _name = 'stock.discrepancy'
    _description = 'Stock Discrepancy'

    inventory_id = fields.Many2one('product.product', string='Inventory', required=True)
    comments = fields.Text(string='Comments')

class AssignedInventory(models.Model):
    _name = 'assigned.inventory'
    _description = 'Assigned Inventory'

    date = fields.Date(string='Date', default=fields.Date.today(), required=True)
    inventory_id = fields.Many2one('product.product', string='Inventory', required=True)
    quantity = fields.Integer(string='Quantity', default=1)
    comments = fields.Text(string='Comments')

class FaultInventory(models.Model):
    _name = 'fault.inventory'
    _description = 'Fault Inventory'

    date = fields.Date(string='Date', default=fields.Date.today(), required=True)
    inventory_id = fields.Many2one('product.product', string='Inventory', required=True)
    comments = fields.Text(string='Comments')

class ProductProduct(models.Model):
    _inherit = 'product.product'

    category = fields.Selection([('A', 'Category A'), ('B', 'Category B'), ('C', 'Category C'), ('D', 'Category D')], string='Category')
