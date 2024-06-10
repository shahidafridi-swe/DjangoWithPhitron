from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import AlbumForm
from .models import Album

# def addAlbum(request):
#     if request.method == 'POST':
#         form = AlbumForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('home')
#     else:
#         form = AlbumForm()
#     context = {'form' : form, 'current_page': 'add_album'}
#     return render(request, 'album/add_album.html', context)

class AddAlbumView(CreateView):
    # model = Album
    template_name= 'album/add_album.html'
    form_class = AlbumForm
    success_url = reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'add_album'
        return context


#-----------------------------------------------------------
    
# def updateAlbum(request, id):
#     album = Album.objects.get(pk=id)
#     form = AlbumForm(instance=album)
#     if request.method == 'POST':
#         form = AlbumForm(request.POST, instance=album)
#         form.save()
#         return redirect('home')
#     form_type = 'update'
#     context = {'form' : form, 'form_type':form_type}
#     return render(request, 'album/add_album.html', context)


class UpdateAlbumView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album/add_album.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_type'] = 'update'
        return context

#-----------------------------------------------------------


# def deleteAlbum(request, id):
#     album = Album.objects.get(pk=id)
#     album.delete()
#     return redirect('home')

class DeleteAlbumView(DeleteView):
    model = Album
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'