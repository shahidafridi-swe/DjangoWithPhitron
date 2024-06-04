from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('update_profile/', views.updateUser, name='update_profile'),
    path('change_password/', views.changePassword, name='change_password'),
    path('profile/', views.userProfile, name='profile'),
]
