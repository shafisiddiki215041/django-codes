from django.shortcuts import render, redirect
from . import models

# Create your views here.
def home(request):
    student = models.Students.objects.all()
    return render(request,'home.html',{"data":student})


def delete_student(request, roll):
    std = models.Students.objects.get(pk = roll).delete()
    # print(std)
    return redirect('homepage')
    