from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my Blog!")

def about(request):
    return HttpResponse("Welcome to my Blog about!")