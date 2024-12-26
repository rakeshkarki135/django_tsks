from django.urls import path 
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView



urlpatterns = [
     path('', StudentView.as_view(), name="index"),
     path('<int:id>', StudentView.as_view(), name="student"),
     path('register', RegisterView.as_view(), name="register"),
     path('login', LoginView.as_view(), name="login"),
     path('profile', ProfileView.as_view(), name="profile"),
     path('logout', LogoutView.as_view(), name="logout"),
     path('token', TokenObtainPairView.as_view()),
     path('token/refresh', TokenRefreshView.as_view()),
     
]