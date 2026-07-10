from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def post_details(request, post_id):
    return HttpResponse(f"<h1>Post Details</h1><p>This is the details page for post with ID: {post_id}.</p>")

def user_profile(request, username):
    return HttpResponse(f"<h1>User Profile</h1><p>This is the profile page for user: {username}.</p>")

def article_by_year(request, year):
    return HttpResponse(f"<h1>Articles by Year</h1><p>This is the page for articles published in {year}.</p>")

# def article_details(request, year, month, day):
#     return HttpResponse(f"<h1>Article Details</h1><p>This is the details page for the article published on {year}-{month}-{day}.</p>")

def article_details(request, **kwargs):
    return HttpResponse(f"<h1>Article Details : {kwargs}</h1>")