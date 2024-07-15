from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('cars/',views.CarList.as_view()),
    path('profile/',views.profile,name='profile'),
    # path('profile_detail_edit/<int:pk>/',views.profile_detail_edit.as_view(),name='profile_detail_edit'),
    path('profile_detail_edit/',views.profile_detail_edit,name='profile_detail_edit'),
    path('details/<int:id>/',views.details.as_view(),name='details'),
    path('show_buy_car/<int:id>/',views.show_buy_car.as_view(),name='show_buy_car'),
    # path('show_buy_car/<int:id>/',views.show_buy_car,name='show_buy_car')
]
