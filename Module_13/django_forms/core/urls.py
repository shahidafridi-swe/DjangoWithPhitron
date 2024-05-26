from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('form2/', views.form2, name='form2'),
    path('django_form/', views.djangoForm, name='django_form'),
]
