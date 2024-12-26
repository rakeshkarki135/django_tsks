from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Student
from .forms import StudentForm
from .serializer import StudentSerializer, RegisterSerializer
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth import get_user_model
User = get_user_model()



# Create your views here.
class StudentView(APIView):
     student_obj = Student.objects.all()
     
     def permission_checker(self, request):
          if request.method in ["POST","PUT","PATCH","DELETE"] and not request.user.is_authenticated:
               return Response({"error": "authentication credentials not provided"}, status=status.HTTP_401_UNAUTHORIZED)
          return None
          
     
     def get(self, request):
          serializer = StudentSerializer(self.student_obj, many=True)
          student_data = serializer.data
          return Response({'status':200, 'message':'Success', 'payload':serializer.data})
          
          
     def post(self, request):
          permission_error = self.permission_checker(request)
          if permission_error:
               return permission_error
          
          serializer = StudentSerializer(data=request.data)
          if not serializer.is_valid():
               return Response({'status':400, "message":"error occured", "payload":serializer.errors})
          serializer.save()
          return Response({'status':201, 'message':'data inserted', 'payload':serializer.data})
          
          
     def put(self, request): 
          permission_error = self.permission_checker(request)
          if permission_error:
               return permission_error
          
          try:
               student = Student.objects.get(id = request.data['id'])
          except Exception as e:
               return Response({'status':400, 'message':'id not found'})
          
          serializer = StudentSerializer(student, request.data)
          
          if not serializer.is_valid():
               return Response({'status':400, 'message':'something went wrong', 'payload':serializer.errors})
          serializer.save()
          return Response({'status':200, 'message':'success', 'payload':serializer.data})
     

     def patch(self, request):
          permission_error = self.permission_checker(request)
          if permission_error:
               return permission_error
          
          try:
               student = Student.objects.get(id = request.data['id'])
          except Exception as e:
               return Response({'status':400, 'message':"id not found"})
          
          serializer = StudentSerializer(student, request.data, partial=True)
          
          if not serializer.is_valid():
               return Response({'status':400, 'message':'error', 'payload':serializer.errors})
          serializer.save()
          return Response({'status':200, 'message':'success', 'payload':serializer.data})
     
     
     def delete(self, request, id):
          permission_error = self.permission_checker(request)
          if permission_error:
               return permission_error
          
          try:
               student = Student.objects.get(id=id)
               student.delete()
               return Response({'status': 200, "message": "Student deleted successfully"})

          except Student.DoesNotExist:
               return Response({'status': 404, 'message': 'Student with the given ID not found'})

          except Exception as e:
               return Response({'status': 500, 'message': 'An error occurred', 'error': str(e)})
          
     

class RegisterView(APIView):
     def post(self, request):
          serializer = RegisterSerializer(data = request.data)
          
          if serializer.is_valid():
               user = serializer.save()
               return Response({
                    "status":True,
                    "message":"User created Succecssfully",
                    "payload":serializer.data
               }, status=status.HTTP_201_CREATED)
               
          return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
          
          
class LoginView(APIView):
     def post(self, request):
          data = request.data   
          username = data.get("phone_number")
          password = data.get("password")
          
          try:
               user = User.objects.get(phone_number = username)
               if user.check_password(password):
                    refresh = RefreshToken.for_user(user)
                    return Response({
                         "message":"Login Success",
                         "access_token" : str(refresh.access_token),
                         "refresh_token" : str(refresh)
                         
                    })
               
               return Response({"message":"Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
               
          except User.DoesNotExist:
               return Response({"message":"User is not Found"}, status=status.HTTP_404_NOT_FOUND)
          
          
class ProfileView(APIView):
     permission_classes = [IsAuthenticated]
     
     def get(self, request):
          user = request.user  
          serializer = RegisterSerializer(user)
          return Response(serializer.data)
     

class LogoutView(APIView):
     permission_classes=[IsAuthenticated]
     def post(self, request):
          try:
               refresh_token = request.data["refresh_token"]
               token = RefreshToken(refresh_token)
               token.blacklist()
               
               return Response({"message":"Logged out Successfully"}, status=status.HTTP_205_RESET_CONTENT)
          except Exception as e:
               return Response({"error":"Failed to logout the user"}, status=status.HTTP_400_BAD_REQUEST)