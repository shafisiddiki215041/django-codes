from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('signup/',views.signup, name ='signup'),
    path('login/',views.user_login, name ='login'),
    path('logout/',views.user_logout, name ='logout'),
    path('profile/',views.profile, name ='profile'),
    path('profile/pass_change_with/',views.pass_change_with, name ='pass_change_with'),
    path('profile/pass_change_withouth/',views.pass_change_withouth, name ='pass_change_withouth'),
]
