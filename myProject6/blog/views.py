from django.shortcuts import render
from datetime import datetime

# Create your views here.

def blog_details(request):
    post ={
        "title": "My Second Template",
        "description": "Danango is High-level language",
        "author": "None",
        "created_at": datetime(2026,8,13,1,11),
        "comments_count": "5",
        "tags": ["Django","Python","Web Development"],
        "price":100,
        "number":8,
    }
    return render(request,'blog/blog_details.html',{"post":post})