from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('edit/',views.edit_musician.as,name = 'edit_musician'),
    path('add_album/',views.AlbumCreate.as_view(),name ='add_album'),
]
