from odoo import http
from odoo.http import request

class LandingPageController(http.Controller):

    @http.route('/landing_page', type='json', auth='user', website=False)
    def landing_page(self):
        OrderProforma = request.env['order.proforma']
        InboundStock = request.env['inbound.stock']
        AssignedStock = request.env['assigned.stock']
        
        proformas = OrderProforma.search([], order='date desc')
        inbound_stock = InboundStock.search([])
        assigned_stock = AssignedStock.search([])

        return {
            'proformas': [{'order_number': p.order_number, 'date': p.date, 'total_inventory': p.total_inventory} for p in proformas],
            'inbound_stock': [{'inventory_id': i.inventory_id.id, 'quantity': i.quantity} for i in inbound_stock],
            'assigned_stock': [{'inventory_id': a.inventory_id.id, 'quantity': a.quantity} for a in assigned_stock],
        }
