from odoo import http
from odoo.http import request
import json

class CRMUser(http.Controller):

    @http.route('/create_crm_user', auth='public', type="json", method=['POST'], csrf=False)
    def create_crm_user(self, **kw):
        data = json.loads(request.httprequest.data)
        name = data.get('name')
        phone = data.get('phone')
        email = data.get('email')

        if not all([name, phone, email]):
            return {"error": "Please provide name, phone, and email."}

        result = self.create_user(name, phone, email)
        return {"result": result}

    def create_user(self, name, phone, email):  
        existing_user = request.env['res.partner'].search([('email', '=', email)], limit=1)
        if existing_user:
            return "User with this email already exists."
        
        user_data = {
            'name': name,
            'phone': phone,
            'email': email
        }
        new_user = request.env['res.partner'].create(user_data)
        return "User created successfully"



class Testing(http.Controller):
    
    @http.route('/api/testing', auth='public', methods=["GET"], csrf=False)
    def read_user_data(self):
        partner = http.request.env['res.partner'].search([('id','=',"66")],limit=1).read()
        print(partner, 99999999999999999999999999)
        # data=json.dumps(partner)
        return "data"



       
