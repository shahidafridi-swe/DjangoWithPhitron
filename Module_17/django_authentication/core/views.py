from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, UpdateUserForm

def home(request):
    return render(request, 'home.html')


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully !!!')
            print(form.cleaned_data)
            return redirect('register')
        else:
            messages.error(request, 'Your given information is not valid !!!')
            
    else:
        form = RegisterForm()
        
    return render(request, 'register_form.html', {'form' : form})

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successfull !!!')
                return redirect('profile')
            else:
                messages.error(request, 'User not found !!!')
    else:
        form = AuthenticationForm()
    return render(request, 'login_form.html', {'form':form})



def logoutUser(request):
    logout(request)
    messages.info(request, 'Logout successfull !!!')
    return redirect('login')



# @login_required(login_url='login')
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user': request.user})
    else:
        messages.error(request, 'You have to login first !!!')
        return redirect('login')
    
@login_required(login_url='login')
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password changed successfully !!!')
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
        
    return render(request, 'change_password_form.html', {'form':form})
   
@login_required(login_url='login')
def setPassword(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password changed successfully !!!')
            return redirect('profile')
    else:
        form = SetPasswordForm(user=request.user)
        
    return render(request, 'change_password_form.html', {'form':form})


@login_required(login_url='login')
def updateUser(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated successfully !!!')
            print(form.cleaned_data)
            return redirect('profile')
        else:
            messages.error(request, 'Your given information is not valid !!!')
    else:
        form = UpdateUserForm(instance = request.user)
        
    return render(request, 'update_user_form.html', {'form' : form})