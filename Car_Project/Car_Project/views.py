from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from car_model.models import CarModel
from brand_model import models

def home(request, brand_slug=None):
    car = CarModel.objects.all()
    if brand_slug is not None:        
        brand = models.Brand.objects.get(slug = brand_slug)
        car = CarModel.objects.filter(brand =brand)
    brands = models.Brand.objects.all()
    return render(request,'home.html',{'cars':car,'brands':brands})

class login_page(LoginView):
    template_name = 'register_login.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login'
        return context

class logout_page(LogoutView):
    template_name = 'register_login.html'
    
    def get_success_url(self):
        return reverse_lazy('login')
    
    def form_valid(self, form):
        messages.success(self.request, 'Logged out successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Logout'
        return context
    
