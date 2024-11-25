from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('countryapp.urls')),  # Include countryapp URLs
]
