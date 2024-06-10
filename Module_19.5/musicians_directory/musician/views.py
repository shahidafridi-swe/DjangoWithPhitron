from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .forms import MusicianForm
from .models import Musician

# def addMusician(request):
#     if request.method == 'POST':
#         form = MusicianForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('musicians')
#     else:
#         form = MusicianForm()
        
#     context = {'form' : form,'current_page': 'add_musician'}
#     return render(request, 'musician/add_musician.html', context)

class AddMusicianView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician/add_musician.html'
    success_url = reverse_lazy('musicians')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'add_musician'
        return context

#-----------------------------------------------------


# def allMusicians(request):
#     data = Musician.objects.all()
    
#     context = {'musicians' : data, 'current_page': 'musicians'}
#     return render(request, 'musician/musicians.html', context)


class AllMusiciansView(ListView):
    model = Musician
    template_name = 'musician/musicians.html'
    context_object_name = 'musicians'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'musicians'
        return context


#-----------------------------------------------------


# def updateMusician(request, id):
#     musician = Musician.objects.get(pk=id)
#     form = MusicianForm(instance=musician)
    
#     if request.method == 'POST':
#         form = MusicianForm(request.POST,instance=musician)
#         if form.is_valid():
#             form.save()
#             return redirect('musicians')
#     form_type = 'update'
#     context = {'form' : form, 'form_type':form_type}
#     return render(request, 'musician/add_musician.html', context)


class UpdateMusicianView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician/add_musician.html'
    success_url = reverse_lazy('musicians')
    pk_url_kwarg = 'id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_type'] = 'update'
        return context

 
#-----------------------------------------------------


# def deleteMusician(request, id):
#     musician = Musician.objects.get(pk=id)
#     musician.delete()
#     return redirect('musicians')


class DeleteMusicianView(DeleteView):
    model = Musician
    template_name = 'delete.html'
    success_url = reverse_lazy('musicians')
    pk_url_kwarg = 'id'

    
#-----------------------------------------------------


# def detailsMusician(request, id):
#     data = Musician.objects.get(pk=id)
#     context = {'musician': data}
#     return render(request, 'musician/musician_details.html', context)

class DetailsMusicianView(DetailView):
    model = Musician
    context_object_name = 'musician'
    pk_url_kwarg = 'id'
    template_name = 'musician/musician_details.html'