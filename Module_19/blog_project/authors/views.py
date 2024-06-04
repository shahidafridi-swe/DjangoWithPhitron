from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm,UpdateUserForm
from posts.models import Post
# from .forms import AuthorForm


# def addAuthor(request):
#     if request.method == 'POST':
#         form = AuthorForm(request.POST)  
#         if form.is_valid():
#             form.save()
#             return redirect('add_author')
#     else:
#         form = AuthorForm()
#     context = {'form': form}
#     return render(request, 'authors/add_author.html', context)

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
        print('inside post method')
        form = AuthenticationForm(request,request.POST)
        username = request.POST['username']
        password = request.POST['password']
        if form.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                print('inside user is login')
                login(request, user) 
                messages.success(request, 'Logged In Successfull !!!')
                return redirect('posts')
            else:
                print('user is None')
                messages.error(request, 'User Not Found !!!')
                return redirect('login')
        else:
            try:
                User.objects.get(username=username)
                messages.error(request, 'Password incorrect !!!')
            except User.DoesNotExist:
                messages.error(request, 'User Not Found !!!')
    else:
        form = AuthenticationForm()
    print("finished")
    return render(request, 'authors/login_register_form.html', {'form':form, 'type':'Login'})     


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