from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    roll=models.IntegerField()
    #as we know that object is default manager 
    #if we want to change it
    #suppose we want to make student as the manager
    students=models.Manager()
