from django.urls import path
from . import views
urlpatterns = [
    path('add_profile/', views.addProfile, name='add_profile'),
]
