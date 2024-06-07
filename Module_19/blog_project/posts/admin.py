from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'body')
