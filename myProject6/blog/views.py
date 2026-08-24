from django.shortcuts import render
from datetime import datetime

# Create your views here.

def blog_details(request):
    post ={
        "title": "My Second Template",
        "description": "Danango is High-level language",
        "author": "Umair Ahmad",
        "created_at": datetime(2026,8,13,1,11),
        "comments_count": "1",
        "tags": ["Django","Python","Web Development"],
        "price":187.23546,
        "number":8,
    }
    return render(request,'blog/blog_details.html',{"post":post})