from django.shortcuts import render, redirect
from .models import ArtistaDeRua  # Se você tiver o modelo Intervencao, adicione depois
from .forms import ArtistaForm

def index(request):
    artistas = ArtistaDeRua.objects.all()
    # Se você tiver Intervencao, descomente a linha abaixo
    # obras = Intervencao.objects.all()
    
    return render(request, 'biblioteca/index.html', {
        'artistas': artistas,
        # 'obras': obras
    })

def cadastrar_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArtistaForm()
    
    return render(request, 'biblioteca/cadastrar_artista.html', {
        'form': form
    })
