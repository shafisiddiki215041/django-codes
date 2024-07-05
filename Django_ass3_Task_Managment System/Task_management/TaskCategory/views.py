from django.shortcuts import render,redirect
from . import  forms
# Create your views here.
def add_category(request):
    if request.method == 'POST':
        category= forms.Task_cat_Form(request.POST)
        if category.is_valid():
            category.save()
            return redirect('add_category')
    else:
        category= forms.Task_cat_Form()
    return render(request,'add_category.html',{'form':category})