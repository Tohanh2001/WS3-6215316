from django.contrib import admin
from django.urls import path, include  # Add 'include' here



urlpatterns = [
    path('admin/', admin.site.urls),

    # Include the app-level URLs
    path('', include('workshop3_app.urls')),
]
