from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=50)          
    user_profile_image = models.ImageField(upload_to="profile_pic")      
    is_phone_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True)
    
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []
    objects = UserManager()
