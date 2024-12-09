from django.db import models

# Create your models here.
class Student(models.Model):
     name = models.CharField(max_length=100)
     address = models.CharField(max_length=100)
     gender = models.CharField(max_length=100)
     age = models.IntegerField()
     
     
     def __str__(self):
          return self.name
     
