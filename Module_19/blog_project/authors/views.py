from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import RegisterForm,UpdateUserForm
from posts.models import Post


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('posts')
    if request.method == 'POST':
        form = RegisterForm(request.POST)  
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully !!!')
            return redirect('login')
    else:
        form = RegisterForm()
    context = {'form': form, 'type': 'Register'}
    return render(request, 'authors/login_register_form.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('posts')
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        username = request.POST['username']
        password = request.POST['password']
        if form.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user) 
                messages.success(request, 'Logged In Successfull !!!')
                return redirect('posts')
        else:
            try:
                User.objects.get(username=username)
                messages.error(request, 'Password incorrect !!!')
            except User.DoesNotExist:
                messages.error(request, 'User Not Found !!!')
    else:
        form = AuthenticationForm()
    return render(request, 'authors/login_register_form.html', {'form':form, 'type':'Login'})     


class LoginUser(LoginView):
    template_name = 'authors/login_register_form.html'
    
    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect('posts')
    
    def get_success_url(self):
        return reverse_lazy('posts')
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in Successfull !!!')
        return super().form_valid()
    
    def form_invalid(self, form):
        messages.error(self.request, 'Wrong Information')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context 
    


@login_required(login_url='login')
def userProfile(request):
    posts = Post.objects.filter(author=request.user)
    context = {
        'posts' : posts
    }
    return render(request, 'authors/profile.html', context)



@login_required(login_url='login')
def updateUser(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)  
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Updated Successfully !!!')
            return redirect('profile')
    else:
        form = UpdateUserForm(instance=request.user)
    context = {'form': form, 'type': 'Update'}
    return render(request, 'authors/login_register_form.html', context)


@login_required(login_url='login')
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)  
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Successfully !!!')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'authors/change_password_form.html', context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    messages.info(request, 'Logout successfull !!!')
    return redirect('login')