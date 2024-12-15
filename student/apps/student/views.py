from django.shortcuts import render,  HttpResponse, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from .forms import StudentForm

# Create your views here.

class StudentView(APIView):
     student_obj = Student.objects.all()
     
     def get(self, request):
          serializer = StudentSerializer(self.student_obj, many=True)
          student_data = serializer.data
          return Response({'status':200, 'message':'Success', 'payload':serializer.data})
          
          
     def post(self, request):
          serializer = StudentSerializer(data=request.data)
          
          if not serializer.is_valid():
               return Response({'status':400, "message":"error occured", "payload":serializer.errors})
          serializer.save()
          return Response({'status':201, 'message':'data inserted', 'payload':serializer.data})
          
          
     def put(self, request): 
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
          try:
               student = Student.objects.get(id=id)
               student.delete()
               return Response({'status': 200, "message": "Student deleted successfully"})

          except Student.DoesNotExist:
               return Response({'status': 404, 'message': 'Student with the given ID not found'})

          except Exception as e:
               return Response({'status': 500, 'message': 'An error occurred', 'error': str(e)})
     
          
          
          
     