from django.urls import path

from . import views

urlpatterns = [
    path('musicians/', views.allMusicians, name='musicians'),
    path('add_musician/', views.addMusician, name='add_musician'),
    path('update_musician/<int:id>/', views.updateMusician, name='update_musician'),
    path('delete_musician/<int:id>/', views.deleteMusician, name='delete_musician'),
    path('details_musician/<int:id>/', views.detailsMusician, name='details_musician'),
]

