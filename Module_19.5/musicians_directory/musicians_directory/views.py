from django.shortcuts import render 
from album.models import Album


def home(request):
    data = Album.objects.all()
    context = {'albums': data,'current_page': 'home'}
    return render(request, 'home.html', context)