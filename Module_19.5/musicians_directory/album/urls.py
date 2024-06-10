from django.urls import path

from . import views

urlpatterns = [
    # path('add_album/', views.addAlbum, name="add_album"),
    path('add_album/', views.AddAlbumView.as_view(), name="add_album"),
    # path('update_album/<int:id>/', views.updateAlbum, name="update_album"),
    path('update_album/<int:id>/', views.UpdateAlbumView.as_view(), name="update_album"),
    # path('delete_album/<int:id>/', views.deleteAlbum, name="delete_album"),
    path('delete_album/<int:id>/', views.DeleteAlbumView.as_view(), name="delete_album"),
]

