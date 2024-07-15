from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
# Create your views here.

def register(request):
    form = forms.RegistrationForm()
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Accoutn Create Successfully')
            return redirect('login')
    return render(request,'register_login.html',{'form':form,'type':'Registration'})     
