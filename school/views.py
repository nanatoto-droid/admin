from django.shortcuts import render, redirect
from .models import Student

# List students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# Create school
def student_create(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            age=request.POST['age'],
            course=request.POST['course']
        )
        return redirect('student_list')
    return render(request, 'student_form.html')

# Update school
def student_update(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.age = request.POST['age']
        student.course = request.POST['course']
        student.save()
        return redirect('student_list')
    return render(request, 'student_form.html', {'school': student})

# Delete school
def student_delete(request, id):
    Student.objects.get(id=id).delete()
    return redirect('student_list')
