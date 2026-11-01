from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my shop home!")

def products(request):
    return HttpResponse("Welcome to my shop products!")