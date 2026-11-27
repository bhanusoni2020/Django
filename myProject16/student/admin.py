from django.contrib import admin
from student.models import students
# Register your models here.

@admin.register(students)
class stuAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'city')
    search_fields = ('name', 'age', 'city')
    list_filter = ('name', 'age', 'city')
    ordering = ('name',)