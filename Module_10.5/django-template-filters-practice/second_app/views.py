from django.shortcuts import render

def secondHome(request):
    return render(request, 'second_app/second_app_home.html')

def products(request):
    return render(request, 'second_app/products.html')

def users(request):
    return render(request, 'second_app/users.html')
