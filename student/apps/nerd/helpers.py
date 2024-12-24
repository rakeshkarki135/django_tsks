import requests
import random

from django.conf import settings


def send_otp_to_phone(phone_number):
    try:
        otp = random.randint(1000, 9999)
        url = f"https://2factor.in/API/V1/{api_key}/SMS/{phone_number}/{otp}"
        
    except Exception as e:
        return None