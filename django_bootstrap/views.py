from django.shortcuts import render

def index(request):
    context = {
        'judul' : 'Funday',
        'subjudul' : 'Selamat Datang',
        'content_jumbotron': 'Halo ini adalah project pribadi aku.',
    }
    return render(request, 'index.html', context)