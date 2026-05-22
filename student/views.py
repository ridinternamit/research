from django.shortcuts import render, redirect
from .models import Student

def home(request):
    data = Student.objects.all()
    return render(request, 'home.html', {'data': data})


def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            course=request.POST['course'],
            marks=request.POST['marks']
        )
        return redirect('/')
    return render(request, 'add.html')