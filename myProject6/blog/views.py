from django.shortcuts import render
from datetime import datetime

def blog_details(request):
    post = {
        "title": "My sec templates post",
        "descriptions": "Django is a high level python web freamework",
        "author": "yes",
        "created_at": datetime(2022,9,29,10,10),
        "comments_count":6,
        "tags":["Django", "python", "web development"],
        "price":100,
        "number":7,


    }

    return render(request, 'blog/blog_details.html', {"post":post})