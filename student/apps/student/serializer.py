from .models import *
from rest_framework import serializers

from django.contrib.auth import get_user_model
User = get_user_model()



class StudentSerializer(serializers.ModelSerializer):
     class Meta:
          model = Student
          fields = '__all__'
          

class RegisterSerializer(serializers.ModelSerializer):
     confirm_password = serializers.CharField(write_only=True)
     class Meta:
          model = User
          fields = ["phone_number", "email","password","confirm_password"]
          
     def validate(self, data):
          if data["password"] != data["confirm_password"]:
               raise serializers.ValidationError("Password doe not match")
          return data
     
     def create(self, validated_data):
          user = User.objects.create_user(
               phone_number = validated_data["phone_number"],
               email = validated_data["email"],
               password = validated_data["password"]
          )
          return user


          
          
     
          