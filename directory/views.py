from django.shortcuts import render, get_object_or_404
from .models import Teacher, Student

# Create your views here.

def home(request):
    return render(request, 'directory/home.html')

def all_students(request):
    students = Student.objects.all()
    return render(request, 'directory/students.html', {'students': students})

def all_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'directory/teachers.html', {'teachers': teachers})

def student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    students = Student.objects.all()
    return render(request, 'directory/student_details.html', {'student': student,'students': students})

def teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    teachers = Teacher.objects.all()
    return render(request, 'directory/teacher_details.html', {'teacher': teacher,'teachers': teachers})