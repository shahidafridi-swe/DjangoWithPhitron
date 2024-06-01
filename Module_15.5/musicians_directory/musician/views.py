from django.shortcuts import render, redirect
from .forms import MusicianForm

from .models import Musician

def addMusician(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musicians')
    else:
        form = MusicianForm()
        
    context = {'form' : form,'current_page': 'add_musician'}
    return render(request, 'musician/add_musician.html', context)

def allMusicians(request):
    data = Musician.objects.all()
    
    context = {'musicians' : data, 'current_page': 'musicians'}
    return render(request, 'musician/musicians.html', context)

def updateMusician(request, id):
    musician = Musician.objects.get(pk=id)
    form = MusicianForm(instance=musician)
    
    if request.method == 'POST':
        form = MusicianForm(request.POST,instance=musician)
        if form.is_valid():
            form.save()
            return redirect('musicians')
    form_type = 'update'
    context = {'form' : form, 'form_type':form_type}
    return render(request, 'musician/add_musician.html', context)

def deleteMusician(request, id):
    musician = Musician.objects.get(pk=id)
    musician.delete()
    return redirect('musicians')
    

def detailsMusician(request, id):
    data = Musician.objects.get(pk=id)
    context = {'musician': data}
    return render(request, 'musician/musician_details.html', context)