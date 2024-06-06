from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.registerUser, name='register'),
    # path('login/', views.loginUser, name='login'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logoutUser, name='logout'),
    # path('logout/', LogoutView.as_view, name='logout'),
    path('update_profile/', views.updateUser, name='update_profile'),
    path('change_password/', views.changePassword, name='change_password'),
    path('profile/', views.userProfile, name='profile'),
]
