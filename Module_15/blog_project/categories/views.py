from django.shortcuts import render, redirect

from .forms import CategoryForm

def addCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_category')
    else:
        form = CategoryForm()
    context = {'form' : form}
    
    return render(request, 'categories/add_category.html', context)