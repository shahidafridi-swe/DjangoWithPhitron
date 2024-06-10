from django.urls import path

from . import views

urlpatterns = [
    # path('', views.allMusicians, name='musicians'),
    path('', views.AllMusiciansView.as_view(), name='musicians'),
    # path('add_musician/', views.addMusician, name='add_musician'),
    path('add_musician/', views.AddMusicianView.as_view(), name='add_musician'),
    # path('update_musician/<int:id>/', views.updateMusician, name='update_musician'),
    path('update_musician/<int:id>/', views.UpdateMusicianView.as_view(), name='update_musician'),
    # path('delete_musician/<int:id>/', views.deleteMusician, name='delete_musician'),
    path('delete_musician/<int:id>/', views.DeleteMusicianView.as_view(), name='delete_musician'),
    # path('details_musician/<int:id>/', views.detailsMusician, name='details_musician'),
    path('details_musician/<int:id>/', views.DetailsMusicianView.as_view(), name='details_musician'),
]

