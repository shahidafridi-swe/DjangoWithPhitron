from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import Album

def addAlbum(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = AlbumForm()
    context = {'form' : form, 'current_page': 'add_album'}
    return render(request, 'album/add_album.html', context)
    
def updateAlbum(request, id):
    album = Album.objects.get(pk=id)
    form = AlbumForm(instance=album)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        form.save()
        return redirect('home')
    form_type = 'update'
    context = {'form' : form, 'form_type':form_type}
    return render(request, 'album/add_album.html', context)

def deleteAlbum(request, id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect('home')