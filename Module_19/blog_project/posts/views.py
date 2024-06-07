from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView,DeleteView, DetailView, FormView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm, CommentForm
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
    

def postDetails(request, id):
    post = Post.objects.get(pk=id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_details', id=post.id)
    else:
        form = CommentForm()
        
    context = {
        'post' : post,
        'comment_form' : form
    }
    return render(request, 'posts/post_details.html', context)

class PostDetails(DetailView):
    model = Post
    template_name = 'posts/post_details.html'
    pk_url_kwarg = 'id'
    
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        return self.get(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_form = CommentForm()
        context['comment_form'] = comment_form
        return context
        
    
    
    
    
# class PostDetails(DetailView, FormView):
#     model = Post
#     template_name = 'posts/post_details.html'
#     context_object_name = 'post'
#     form_class = CommentForm

#     def get_success_url(self):
#         return reverse_lazy('post_details', kwargs={'id': self.object.id})

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['comment_form'] = self.get_form()
#         return context

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()  # get the post object
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

#     def form_valid(self, form):
#         comment = form.save(commit=False)
#         comment.post = self.object
#         comment.save()
#         return redirect(self.get_success_url())