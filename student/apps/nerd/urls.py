from django.urls import path 
from .views import *

urlpatterns = [
    path("", index, name="list-student"),
    path("add", student, name="add-student"),
    path("add/<int:student_id>", student, name="update-student"),
    path("delete/<int:student_id>", delete_std, name="delete-student"),
    
]