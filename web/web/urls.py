from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1', include('djoser.urls')), #get api user
    path('api/v1', include('djoser.urls.authtoken')), #get api user token
]
