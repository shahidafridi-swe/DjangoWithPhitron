from django.shortcuts import render, redirect
from .forms import Form_1, Form_2
# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def form_1(request):
    if request.method == 'POST':
        form = Form_1(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('form_1')
    else:
        form = Form_1()
    
    return render(request, 'core/form_1.html', {'form':form})


def form_2(request):
    if request.method == 'POST':
        form = Form_2(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            profile_image = form.cleaned_data['profile_image']
            with open('./uploads/files/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
                    
            with open('./uploads/images/' + profile_image.name, 'wb+') as destination:
                for chunk in profile_image.chunks():
                    destination.write(chunk)
                    
            print(form.cleaned_data)
            return redirect('form_2')
    else:
        form = Form_2()
    
    return render(request, 'core/form_2.html', {'form':form})