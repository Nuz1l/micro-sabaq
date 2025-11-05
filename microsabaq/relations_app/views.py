from django.shortcuts import render
from .models import Student

def students_list(request):
    students = Student.objects.select_related('group').prefetch_related('clubs').all().order_by('last_name', 'first_name')
    return render(request, 'students.html', {'students': students})
