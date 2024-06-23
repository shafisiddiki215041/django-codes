from django.contrib import admin
from django.urls import path, include
# from views.py import contact
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact),
    path("first_app/",include("first_app.urls")),
    path("", views.Home)
]
