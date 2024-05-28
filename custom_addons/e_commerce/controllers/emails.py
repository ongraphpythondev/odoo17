from odoo import http
from odoo.tools import email_tools
class CustomEmailController(http.Controller):

    @http.route('/custom/send_email', type='http', auth='user', methods=['POST'])
    def send_email_api(self, **post_data):
        # Extract necessary data from the POST request
        recipient_email = post_data.get('recipient_email')
        subject = post_data.get('subject')
        body = post_data.get('body')

        # Send the email
        email_tools.email_send(recipient_email, subject, body)
        
        return "Email sent successfully"
