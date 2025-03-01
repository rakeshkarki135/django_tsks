
from django.contrib.auth.base_user import BaseUserManager

# we need to modify user and superuser
class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("phone_number is required")
        
        if "email" in extra_fields:
            extra_fields["email"] = self.normalize_email(extra_fields["email"])
            
        user = self.model(phone_number = phone_number, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        
        return user
    
    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        # to avoid error caused by circular import
        from .models import Superuser
        
        superuser = Superuser.objects.create(phone_number = phone_number, **extra_fields)
        superuser.set_password(password)
        superuser.save(using=self._db)
        
        return superuser
        
        


