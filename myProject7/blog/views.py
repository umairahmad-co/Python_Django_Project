from django.shortcuts import render
from datetime import datetime

# Create your views here.

def blog_list(request):
    blogs=[
        {"title":"Django Basics",
         "is_featured":True,
         "author":"UMAIR",
         
        },
        {"title":"Django Intermediate",
         "is_featured":False,
         "author":"",
         
        },
        {"title":"Django Advanced",
         "is_featured":True,
         "author":"ALI",
         
        },
    ]
    
    context={
        "blog":blogs,
        "today":datetime.now(),
        "html_code":"<h1>Welcome to my blog</h1>",
        
    }
    return render(request, 'blog/blog_list.html', context)
