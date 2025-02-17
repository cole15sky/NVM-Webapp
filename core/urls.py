
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', include('home.urls')),
    path('aboutUs/', include('about.urls')),
    path('academic/', include('academic.urls')),
    path('admissions/', include('admissions.urls')),
    path('contactus/', include('contactus.urls')),
]