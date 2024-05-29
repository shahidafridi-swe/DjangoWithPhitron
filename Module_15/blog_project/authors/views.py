from django.shortcuts import render, redirect
from .forms import AuthorForm


def addAuthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('add_author')
    else:
        form = AuthorForm()
    context = {'form': form}
    return render(request, 'authors/add_author.html', context)