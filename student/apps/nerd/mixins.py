from django.conf import settings  
from twilio.rest import Client 

class MessageHandler:
    phone_number = None
    otp = None
    
    def __init__(self, phone_number, otp):
        self.phone_number = phone_number
        self.otp = otp
        
    
    def send_otp(self):
        client = Client(settings.ACCOUNT_SID, settings.ACCOUNT_AUTH)
        
        message = client.messages.create(
            body=f"your otp is {self.otp}",
            from_=,
            to=
        )