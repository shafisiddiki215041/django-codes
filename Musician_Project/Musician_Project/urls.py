from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('musician/',include('musician.urls')),
    path('album/',include('album.urls')),
    path('login/',views.LoginViewOn.as_view(),name='login'),
    path('logout/',views.UserLogOut.as_view(),name='user_logout'),
    # path('profile/',views.profile,name='profile'),
    path('profile/',views.MusicianListView.as_view(),name='profile'),
]
