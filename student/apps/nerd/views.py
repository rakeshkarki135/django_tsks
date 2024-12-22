from django.shortcuts import render, redirect, get_object_or_404
from apps.student.models import Student
from django.contrib import messages     
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators  import login_required

# Create your views here.

def register_user(request):
    if request.method == "POST":
        firstName = request.POST.get("firstname")
        username = request.POST.get("username") 
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmPassword = request.POST.get("confirm-password")
        
        if password != confirmPassword:
            messages.error(request, "Recheck your Password")
            return redirect("register-user")
        
        try:
            if User.objects.filter(username = username).exists():
                messages.info(request, f"User with username {username} already Exists")
                return redirect("register-user")
            
            if User.objects.filter(email = email).exists():
                messages.info(request, f"User with email {email} already Exists")
                return redirect("register-user")
            
            
            user = User.objects.create(
                                first_name = firstName,
                                username = username,
                                email = email,
                                )
            
            user.set_password(password)
            user.save()
            return redirect("login")
                                
            
        except User.DoesNotExist:
            messages.error(request, "Error occured while creating Account")
            
    return render(request, "register.html")
    

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        try:
            if "@" in username:
                user_obj = get_object_or_404(User, email=username)
                
                if user_obj is None:
                    messages.error(request, "User doesnot Exist")
                    return redirect("login-user")
                
                username = user_obj.username
            else:
                if not User.objects.filter(username = username).exists():
                    messages.info(request, "User doesnot Exist")
                    return redirect("login-user")
                
            user = authenticate(username = username, password = password)
            if user is None:
                messages.info(request, "Invalid Credentails")
                return redirect("login-user")
            
            login(request, user)
            return redirect("list-student")
                
        except User.DoesNotExist:
            messages.error("User doesnot Exist")
            return redirect("login-user")
        
    return render(request, "login.html")
    
def index(request):
    student = Student.objects.all()
    return render(request, "index.html", {"students":student})


@login_required
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

@login_required
def delete_std(request, student_id):
    try:
        student_obj = get_object_or_404(Student, id=student_id)
        
        if student_obj:
            student_obj.delete()
            messages.info(request, f"Successfully deleted student named {student_obj.name}")
            return redirect("list-student")
    except Student.DoesNotExist:
        messages.info("Student is not Found")
        return redirect("list-student")
    
@login_required
def logout_user(request):
    logout(request)
    return redirect("login-user")