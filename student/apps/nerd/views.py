from django.shortcuts import render, redirect, get_object_or_404
from apps.student.models import Student
from django.contrib import messages     

# Create your views here.

def index(request):
    student = Student.objects.all()
    return render(request, "index.html", {"students":student})


def student(request, student_id=None):
    if student_id:
        student_obj = get_object_or_404(Student, id=student_id)
    else:
        student_obj = None
    
    if request.method == "POST":
        name = request.POST.get("name","")
        address = request.POST.get("address","")
        gender = request.POST.get("gender","")
        age = request.POST.get("age","")
        
        try:
            if student_obj: 
                student_obj.name = name
                student_obj.address = address
                student_obj.gender = gender
                student_obj.age = age
                
                student_obj.save()
                return redirect("list-student")
            
            else:
                student_obj = Student.objects.create(
                    name = name,
                    address = address,
                    gender = gender,
                    age = age
                )
                return redirect("list-student")
            
        except Exception as e:
            print(f"error occured while creating student : {e}")
            
        
    return render(request, "studentform.html", {'student':student_obj})


def delete_std(request, student_id):
    try:
        student_obj = get_object_or_404(Student, id=student_id)
        
        if student_obj:
            student_obj.delete()
            messages.info(request, f"Successfully deleted student named {student_obj.name}")
            return redirect("list-student")
    except Student.DoesNotExist:
        pass