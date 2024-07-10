from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):
    signup_form = RegistrationForm()
    if request.method == 'POST':
        signup_form = RegistrationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, 'Accout create Successfully')
            return redirect('login')
    return render(request,'signup.html',{'form':signup_form})

def user_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username= user_name, password=user_pass)
            if user is not None:
                messages.success(request, 'Logged In Successfully')
                login(request, user)
                return redirect('profile')
    return render(request,'login.html',{'form':form})    

@login_required
def profile(request):
    return render(request,'profile.html',{'name':request.user})

@login_required
def pass_change_with(request):
    form= PasswordChangeForm(user= request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user =request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,'Password Update Successfully')
            return redirect('profile')
    return render(request,'pass_change.html',{'form':form})

def pass_change_withouth(request):
    form= SetPasswordForm(user= request.user)
    if request.method == 'POST':
        form = SetPasswordForm(user =request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,'Password Update Successfully')
            return redirect('profile')
    return render(request,'pass_change.html',{'form':form})

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('home')