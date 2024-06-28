from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name  ='about'),
    path('form/', views.submitform, name  ='submit_form'),
    path('django_form/', views.PasswordValidation, name  ='django_form'),
]
