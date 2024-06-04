from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('category/<slug:category_slug>/', views.posts, name='category_wise_posts'),
    path('add_post/', views.addPost, name='add_post'),
    path('update_post/<int:id>', views.updatePost, name='update_post'),
    path('delete_post/<int:id>', views.deletePost, name='delete_post'),
    
]
