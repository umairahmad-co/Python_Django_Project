from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home(request):
    return HttpResponse("Hello, World! This is the home page of the blog app.") 


def about(request):
    return HttpResponse("This is the about page of the blog app.")