from django.shortcuts import render, redirect

from .forms import ProfileForm

def addProfile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('add_profile')
    else:
        form = ProfileForm()
    context = {'form': form}
    return render(request, 'profiles/add_profile.html', context)