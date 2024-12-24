from django.db import models

# Create your models here.

class StudentManager(models.Manager):
     def get_queryset(self):
          return super().get_queryset().filter(is_deleted=False)
     
     
class Student(models.Model):
     name = models.CharField(max_length=100)
     address = models.CharField(max_length=100)
     gender = models.CharField(max_length=100)
     age = models.IntegerField()
     is_deleted = models.BooleanField(default=False)
     
     objects = StudentManager()
     admin_objects = models.Manager()
     
     
     def __str__(self):
          return self.name
     
