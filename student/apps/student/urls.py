from django.urls import path 
from .views import *



urlpatterns = [
     path('', StudentView.as_view(), name="index"),
     path('<int:id>', StudentView.as_view(), name="student"),
]