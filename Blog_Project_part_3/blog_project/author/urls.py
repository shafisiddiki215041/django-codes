from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('register/', views.register, name = 'register'),
    # path('user_login/', views.user_login, name = 'user_login'),
    path('user_login/', views.User_loginView.as_view(), name = 'user_login'),
    # path('user_logout/', views.user_logout, name = 'user_logout'),
    path('logout/', views.UserLogOUt.as_view(), name = 'user_logout'),
    path('profile/', views.profile, name = 'profile'),
    path('profile/edit_profile/', views.edit_profile, name = 'edit_profile'),
    path('profile/edit_profile/pass_change/',views.pass_change, name ='pass_change')

]
