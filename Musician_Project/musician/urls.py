from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('edit_musician/<int:id>',views.edit_musician.as_view(),name = 'edit_musician_name'),
    path('edit_album/<int:id>',views.edit_album.as_view(),name = 'edit_album'),
    path('add_musician/',views.AddMusician_create.as_view(), name='add_musician'),
    path('delete/<int:id>',views.delete.as_view(), name='delete'),
]
