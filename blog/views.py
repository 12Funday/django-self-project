from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'Blog',
        'subjudul': 'Selamat datang di Blog',
    }
    return render(request, 'blog/index.html', context)