from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home(request):
    return HttpResponse("Hello, World! This is the home page of the shop app.") 

def products(request):
    return HttpResponse("This is the products page of the shop app.")