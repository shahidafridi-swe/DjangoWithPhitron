from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def posts(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'posts/posts.html', context)


def addPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = PostForm()
    context = {'form' : form}
    
    return render(request, 'posts/add_post.html', context)

def updatePost(request, id):
    post = Post.objects.get(pk=id)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    
    context = {'form' : form}
    
    return render(request, 'posts/add_post.html', context)

def deletePost(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('posts')