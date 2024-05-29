from django.urls import path
from . import views
urlpatterns = [
    path('add_author/', views.addAuthor, name='add_author'),
]
