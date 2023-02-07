from django.shortcuts import render
from .models import Student
# Create your views here.
def fun(request):
    student_data=Student.students.all()
    # student_data=Student.objects.all()

    #here object is bydefault manager and this is important point
    return render(request,'app/home.html',{'student_data':student_data})
