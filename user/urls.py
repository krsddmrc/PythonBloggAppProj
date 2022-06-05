from re import template
from django.contrib import admin
from django.urls import path
from .views import home,register
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', home, name="home"),
   path('register', register, name="register"),   
   path('change-password', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'),  name="regist"),   
  
]