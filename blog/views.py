from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

def blog(request):
    return HttpResponse("this is a blog page")
    
def post_list(request):
    return HttpResponse("this is post_list page")
    # Create your views here.
def post_create(request):
    return HttpResponse("this is post_create page")

def post_update(request):
    return HttpResponse("this is post_update page")

def post_delete(request):
    return HttpResponse("this is post_delete page")      