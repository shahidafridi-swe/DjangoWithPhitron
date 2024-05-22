from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('first_app.urls')),
    path('second_app/', include('second_app.urls')),
]
