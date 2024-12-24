from django.contrib import admin
from .models import *

# Register your models here.
class CustomuserAdmin(admin.ModelAdmin):
    list_display = ["phone_number","email","user_bio","first_name"]
    search_fields = ["phone_number","email"]
    list_filter = ["created_at"]
admin.site.register(CustomUser)


class SuperuserAdmin(admin.ModelAdmin):
    list_display = ["phone_number","email","is_active","is_staff","is_superuser"]
    search_fields = ["phone_number","email"]
    list_filter = ["is_active"]
admin.site.register(Superuser, SuperuserAdmin)
