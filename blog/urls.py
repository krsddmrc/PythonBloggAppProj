from cgitb import html
from django.contrib import admin
from django.urls import path
from .views import blog, post_list, post_create, post_update, post_delete

urlpatterns = [
   path('', blog, name="blog"),
   path('post_list', post_list, name="post_list"),
   path('post_create', post_create, name="post_create"),
   path('post_update', post_update, name="post_update"),
   path('post_delete', post_delete, name="post_delete"),
   
]