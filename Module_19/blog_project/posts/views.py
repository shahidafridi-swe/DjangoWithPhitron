from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
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


# @login_required(login_url='login')
# def addPost(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.instance.author = request.user
#             form.save()
#             return redirect('posts')
#     else:
#         form = PostForm()
#     context = {'form' : form, 'type': 'Add'}
    
#     return render(request, 'posts/add_post.html', context)

# @method_decorator(login_required, name='dispatch') login required class based decorator
class AddPost(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/add_post.html'
    success_url = reverse_lazy('posts')
    login_url = 'login'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Add'
        return context

 
# @login_required(login_url='login')
# def updatePost(request, id):
#     post = Post.objects.get(pk=id)
#     if(post.author != request.user):
#         return redirect('posts')
#     form = PostForm(instance=post)
#     if request.method == 'POST':
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('posts')
#     context = {'form' : form, 'type': 'Update'}
#     return render(request, 'posts/add_post.html', context)


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/add_post.html'
    success_url = reverse_lazy('posts')
    login_url = 'login'
    pk_url_kwarg = 'id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Update'
        return context

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user



# @login_required(login_url='login')
# def deletePost(request, id):
#     post = Post.objects.get(pk=id)
#     if(post.author != request.user):
#         return redirect('posts')
#     post.delete()
#     return redirect('posts')

class DeletePost(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('posts')
    login_url = 'login'
    pk_url_kwarg = 'id'
    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
    