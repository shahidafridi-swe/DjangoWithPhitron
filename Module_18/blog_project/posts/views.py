from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from categories.models import Category

def posts(request, category_slug = None):
    posts = Post.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        posts = Post.objects.filter(category=category)
    
    categories = Category.objects.all()
    context = {
        'posts' : posts,
        'categories':categories
    }
    return render(request, 'posts/posts.html', context)


@login_required(login_url='login')
def addPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('posts')
    else:
        form = PostForm()
    context = {'form' : form, 'type': 'Add'}
    
    return render(request, 'posts/add_post.html', context)
 
@login_required(login_url='login')
def updatePost(request, id):
    post = Post.objects.get(pk=id)
    if(post.author != request.user):
        return redirect('posts')
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('posts')
        
    context = {'form' : form, 'type': 'Update'}
    
    return render(request, 'posts/add_post.html', context)

@login_required(login_url='login')
def deletePost(request, id):
    post = Post.objects.get(pk=id)
    if(post.author != request.user):
        return redirect('posts')
    post.delete()
    return redirect('posts')