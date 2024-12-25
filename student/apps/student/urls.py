from django.urls import path 
from .views import *



urlpatterns = [
     path('', StudentView.as_view(), name="index"),
     path('<int:id>', StudentView.as_view(), name="student"),
     path('register', RegisterView.as_view(), name="register"),
     path('login', LoginView.as_view(), name="login"),
]