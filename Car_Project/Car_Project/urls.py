from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('brand_model/',include('brand_model.urls')),
    path('car_model/',include('car_model.urls')),
    path('login/',views.login_page.as_view(), name = 'login'),
    path('logout/',views.logout_page.as_view(), name = 'logout'),
    path('user/',include('user.urls')),
    path('',views.home, name = 'home'),
    path('name_wise_show/<slug:brand_slug>/',views.home, name = 'name_wise_show'),
    # path('name_wise_show/<int:id>/',views.home, name = 'name_wise_show'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)