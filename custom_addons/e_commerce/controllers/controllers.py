from odoo import http
from odoo.http import request
import json
import base64


class ProductAPI(http.Controller):

    @http.route('/api/create_product', type='http', auth='public', methods=['POST'], csrf=False)
    def create_product(self, **kw):
        name = kw.get('name')
        description = kw.get('description')
        price = kw.get('price')
        quantity = kw.get('quantity')
        category = kw.get('category')
        image = kw.get('image')

        print(category,444444444444444444444)
        
        category = request.env['ecommerce.category'].search([('name', '=', category)], limit=1)
        if not category:
            return "Category not found"
        
        # Check if image is provided
        if image:
            # Read binary data from file storage
            image_data = image.read()
            # Decode binary data using base64
            decoded_image = base64.b64decode(image_data)
            print(decoded_image,"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^6")
        else:
            decoded_image = None
        
        product = request.env['ecommerce.product'].create({
            'name': name,
            'description': description,
            'price': price,
            'quantity': quantity,
            'category': category.id,
            'image': decoded_image
        })
        return "Product created successfully!"
  
    
    
class CartAPI(http.Controller):
    @http.route('/add_to_cart', type='json', auth='user')
    def add_to_cart(self, **kw):
        if kw:
            data = kw
            print(data,"&&&&&&&&&&&&&&&&&&&&&&&")
        else:
            data = json.loads(request.httprequest.data)

        product_id = data.get("product_id")
        count = data.get("quantity")
        user_id = data.get("user_id")
        print(product_id,count,user_id,"&&&&&&&&&&&&&&&&&&&&&&&")
        # Check product is out of stock or not
        product = request.env["ecommerce.product"].sudo().browse(product_id)
        if product and (product.quantity - count) >= 0:

            # Check for existing cart or create a new one
            cart = request.env["ecommerce.cart"].sudo().search([("user", "=", user_id)], limit=1)
            if not cart:
                cart = request.env["ecommerce.cart"].sudo().create({"user": user_id})

            # Create cart line
            cartline = request.env["ecommerce.cartline"].sudo().create({
                "product": product_id,
                "quantity": count,
                "cart": cart.id
            })

            # Update product quantity and cart lines
            product.write({"quantity": (product.quantity - count)})
            cart.write({"cart_line": [(4, cartline.id)]})

            msg = "Added to Cart"
        else:
            msg = "Out of stock"

        return msg
    







# for creation user




class CustomCustomer(http.Controller):

    @http.route('/create_customer', auth='public', type="json", method=['POST'], csrf=False)
    def create_custom_customer(self, **kw):
        data = json.loads(request.httprequest.data)
        name = data.get('name')
        password = data.get('password')
        email = data.get('email')

        if not all([name, password, email]):
            return {"error": "Please provide name, password, and email."}

        result = self.create_user(name, password, email)
        return {"result": result}

    def create_user(self, name, password, email):  
        existing_user = request.env['res.partner'].sudo().search([('email', '=', email)], limit=1)
        if existing_user:
            return "User with this email already exists."
        
        user_data = {
            'name': name,
            'password': password,
            'email': email
        }
        new_user = request.env['ecommerce.customer'].sudo().create(user_data)
        return "User created successfully"

    @http.route('/update_customer', auth="public" , type="json", method=['PUT'] , csrf=False)
    def update_customer(self, **kw):
        data=json.loads(request.httprequest.data)
        name=data.get('name')
        password=data.get('password')
        email=data.get('password')
        customer_id=data.get('customer_id')
        if not customer_id:
            return("plz provide the customer_id")
         
        existing_user = request.env['ecommerce.customer'].sudo().browse(customer_id)

        if not existing_user:
            return {"error": "customer not found."}
        if name:
            existing_user.write({'name': name})
        if password:
            existing_user.write({'password': password})
        if email:
            existing_user.write({'email': email})

        return {"result": "User information updated successfully"}

    # @http.route('/delete_customer', auth='public', type="json", method=['POST'], csrf=False)
    # def delete_custom_customer(self, **kw):
    #     data = json.loads(request.httprequest.data)
    #     customuser_id = data.get('customuser_id')
    #     if not customuser_id:
    #         return {"error": "Please provide customuser_id."}
    #     existing_customer = request.env['ecommerce.customer'].sudo().browse(customuser_id)
    #     if not existing_customer:
    #         return {"error": "Customer not found."}
    #     existing_customer.write({'active': False})
    #     existing_customer.unlink()
    #     return {"result": "Customer successfully deactivated and deleted."}

#   by using direct id in url
    @http.route('/delete_customer/<int:user_id>', auth='public', type="json", method=['DELETE'], csrf=False)
    def delete_custom_customer(self, user_id):
        try:
            existing_user = request.env['ecommerce.customer'].sudo().browse(user_id)
            if not existing_user:
                return {"error": "No user found with this ID."}
            existing_user.write({'active': False})
            existing_user.unlink()
            return {"result": "User deleted successfully"}
        except Exception as e:
            return {"error": str(e)}
        

import requests
from odoo import http
from odoo.http import request

class TelegramBot(http.Controller):

    @http.route('/webhook/<string:token>', type='http', auth='public', csrf=False, methods=['POST'])
    def telegram_webhook(self, token, **kw):
        if token == 'telegram_token':
            data = json.loads(request.httprequest.data)
            if 'message' in data:
                chat_id = data['message']['chat']['id']
                print(chat_id,"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                message_text = data['message']['text']
                response_text = self.process_message(message_text)
                self.send_telegram_message(chat_id, response_text)
            return request.make_response("")
        else:
            return request.make_response("")

    def send_telegram_message(self, chat_id, text):
        telegram_api_url = "https://api.telegram.org/bot7156704920:AAE2bvAM7zK3YFJHAPlIUddmDLu_M1PSQrM/sendMessage"
        params = {'chat_id': chat_id, 'text': text}
        response = requests.post(telegram_api_url, json=params)
        return response.json()

    def process_message(self, message_text):
        if message_text == '/start':
            return "Hello! I am your bot. How can I help you today?"
        elif message_text == '/help':
            return "This is a help message. How can I assist you?"
        else:
            return "Sorry, I didn't understand your message. Please try again."






from odoo import http
from odoo.http import request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSenderController(http.Controller):

    @http.route('/send_email', type='json', auth='public', methods=['POST'],csrf=False)
    def send_email(self, **kw):
        # SMTP server details
        smtp_server = 'smtp.gmail.com'
        port = 587  # SMTP port number
        sender_email = 'vaishali.ongraph@gmail.com'  
        password = 'mvxz ehbx tmmf qrha' 
        # Extract data from the request
        data = json.loads(request.httprequest.data)
        customuuser_id = data.get('customer_id')
        subject = data.get('subject')
        body = data.get('body')
        print(customuuser_id,"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55")
        # Fetch customer's email from the database
        customer = request.env['ecommerce.customer'].sudo().browse(customuuser_id)
        receiver_email = customer.customuuser_id.email
        print(receiver_email,"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

        # Compose the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send the email
        try:
            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
                print("Email sent successfully")
        except smtplib.SMTPException as e:
            print("SMTP error occurred:", e)
        except Exception as e:
         print("An unexpected error occurred:", e)


        return {'status': 'success', 'message': 'Email sent successfully.'}
