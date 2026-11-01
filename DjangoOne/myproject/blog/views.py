from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("wellcome to my first django project:  ")
def about(request):
    a = 10 + 10
    return HttpResponse(f"About {a}")