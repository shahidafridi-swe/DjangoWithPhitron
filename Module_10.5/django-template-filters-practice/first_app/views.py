from django.shortcuts import render

from datetime import datetime



def home(request):
    context = {
        'name': "Shahid Afridi",
        'age' : 27,
        'bio' : "I'm a django developer",
        'school' : "amnura high school",
        'published' : datetime.now(),
        'job': "",
        'friends' : [
            {'name': 'galib', 'age': 29},
            {'name': 'nirob', 'age': 23},
            {'name': 'kalin', 'age': 22},
        ],
        'hobby' : ['Travelling', 'Fishing', 'Gardening'],
        'certificate' : """ PSC
                            JSC
                            SSC
                            HSC
                            BSC """,
    }
    return render(request, 'first_app/home.html', context)





def about(request):
    return render(request, 'first_app/about.html')

def contact(request):
    return render(request, 'first_app/contact.html')
