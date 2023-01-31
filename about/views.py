from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'About',
        'subjudul':'Selamat Datang di About page',
    }
    return render(request, 'about/index.html', context)