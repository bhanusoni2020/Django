from django.shortcuts import render
from .models import students
# Create your views here.

def home(request):
    student = students.objects.all()
    return render(request, 'portfolio/blog.html', {'student':student})