from django.shortcuts import render
from .models import Student
# Create your views here.
def fun(request):
    student_data=Student.objects.all()
    return render(request,'app/home.html',{'student_data':student_data})
