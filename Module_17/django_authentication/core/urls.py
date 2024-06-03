from django.urls import path

from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerUser, name='register'),
    path('update_user/', views.updateUser, name='update_user'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.changePassword, name='change_password'),
    path('set_password/', views.setPassword, name='set_password'),
]
