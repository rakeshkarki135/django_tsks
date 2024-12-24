from django.contrib import admin
from .models import *

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ["id","name","address","age","gender"]
admin.site.register(Student, StudentAdmin)
