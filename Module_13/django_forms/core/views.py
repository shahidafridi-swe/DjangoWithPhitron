from django.shortcuts import render
from .forms import ContactForm, ValidationForm

def index(request):
    context={}
    if request.method == 'POST':
        name = request.POST.get('name')    
        email = request.POST.get('email')    
        select = request.POST.get('select')    
        context['name'] = name
        context['email'] = email
        context['select'] = select
         
    return render(request, 'core/index.html',context)


def form(request):
    return render(request, 'core/form.html')

def form2(request):
    return render(request, 'core/form2.html')

def djangoForm(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            
            if form.cleaned_data['file']:
                file = form.cleaned_data['file']
                with open('./core/upload/' + file.name, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)

            print(form.cleaned_data)
            context['form'] = form
    else:
        form = ContactForm()
        context['form'] = form
        
    return render(request, 'core/django_form.html', context)


def validationForm(request):
    form = ValidationForm()

    if request.method == 'POST':
        form = ValidationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, 'core/validation_form.html', {'form': form})
        else:
            return render(request, 'core/validation_form.html', {'form': form})
            
    else:
        return render(request, 'core/validation_form.html', {'form': form})
        