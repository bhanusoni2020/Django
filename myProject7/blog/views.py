from django.shortcuts import render
from datetime import datetime




def blog_list(request):
    blogs =[
        {"title":"Dhango Basics","is_featured":True, "author":"Mohit"},
        {"title":"Django Advanced","is_featured":False, "author":"Bhanu"},
        {"title":"Django REST Framework","is_featured":False, "author":"Vashu"}
    ]
    context = {
        "blogs":blogs,
        "today": datetime.now(),
        "html_code":"<h1>Welcome to My Blog</h1>",
    }
    return render(request, 'blog/blogblog_list.html', context)