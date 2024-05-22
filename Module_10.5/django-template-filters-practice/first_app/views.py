from django.shortcuts import render



def home(request):
    context = {
        'name': "Shahid Afridi"
    }
    return render(request, 'first_app/home.html', context)





def about(request):
    return render(request, 'first_app/about.html')

def contact(request):
    return render(request, 'first_app/contact.html')
