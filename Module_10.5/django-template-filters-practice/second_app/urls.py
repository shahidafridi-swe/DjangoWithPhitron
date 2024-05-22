from django.urls import path 
from . import views

urlpatterns = [
    path('', views.secondHome, name='second_app_home'),
    path('products/', views.products, name='products'),
    path('users/', views.users, name='users'),
]
