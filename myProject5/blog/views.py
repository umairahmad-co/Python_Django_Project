from django.shortcuts import render
from datetime import datetime

# Create your views here.

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def home(request):
    context = {
        'name': "Umair Ahmad",
        'age': 25,
        'skills': ['Python', 'Django', 'JavaScript'],
        'user': User('Ahmad', 30),
        "blog": {
            "title": "Django Template Intro",
            "author":{
                "name":"Akram"
            },
            "content": "<b>This is Blod.</b>",
            "created_at": datetime(2026, 6, 15, 10, 30)
        },
        "empty_value": None
    }
    return render(request, "blog/home.html", context)