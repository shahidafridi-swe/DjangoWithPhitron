from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('category/<slug:category_slug>/', views.posts, name='category_wise_posts'),
    # path('add_post/', views.addPost, name='add_post'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    # path('update_post/<int:id>', views.updatePost, name='update_post'),
    path('update_post/<int:id>', views.UpdatePost.as_view(), name='update_post'),
    # path('delete_post/<int:id>', views.deletePost, name='delete_post'),
    path('delete_post/<int:id>', views.DeletePost.as_view(), name='delete_post'),
    # path('post_details/<int:id>', views.postDetails, name='post_details'),
    path('post_details/<int:id>', views.PostDetails.as_view(), name='post_details'),
    
]
