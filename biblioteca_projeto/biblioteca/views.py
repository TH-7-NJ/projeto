from django.shortcuts import render, redirect
from .models import ArtistaDeRua, IntervencaoArtistica
from .forms import ArtistaForm

def index(request):
    artistas = ArtistaDeRua.objects.all()
    obras = IntervencaoArtistica.objects.filter(visivel=True)
    return render(request, 'biblioteca/index.html', {'artistas': artistas, 'obras': obras})

def cadastrar_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArtistaForm()
    
    return render(request, 'biblioteca/cadastrar.html', {'form': form})
