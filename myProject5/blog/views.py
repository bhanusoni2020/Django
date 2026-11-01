from django.shortcuts import render
from datetime import datetime

class user:
    def __init__(self, name,age):
        self.name = name
        self.age = age

def home(request):
    context = {
        "name":"Bhanu soni",
        "age": 22,
        "skill": ["Pyton", "Django", "React"],
        "User": user("Kumar",30),
        "blog":{
            "title":"Django Template Intro",
            "Author":{
                     "name": "soni",

            },
            "content": "<b>This is Bold</b>",
            "created_at": datetime(2025,8,18,10,30)

        },
        "empty_Value":None,
    }
    return render(request, "blog/home.html",context)
