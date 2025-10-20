from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArtistaForm
from .models import ArtistaDeRua, IntervencaoArtistica, EventoCultural, LocalArtistico, ApoioFinanceiro, MembroEquipe

def index(request):
    artistas = ArtistaDeRua.objects.all()
    obras = IntervencaoArtistica.objects.filter(visivel=True)
    return render(request, 'biblioteca/index.html', {
        'artistas': artistas,
        'obras': obras
    })

def listar_artistas(request):
    artistas = ArtistaDeRua.objects.all()
    return render(request, 'biblioteca/artistas.html', {'artistas': artistas})

def perfil_artista(request, artista_id):
    artista = get_object_or_404(ArtistaDeRua, id=artista_id)
    intervencoes = IntervencaoArtistica.objects.filter(artista=artista, visivel=True)
    return render(request, 'biblioteca/perfil_artista.html', {
        'artista': artista,
        'intervencoes': intervencoes
    })

def galeria(request):
    obras = IntervencaoArtistica.objects.filter(visivel=True)
    return render(request, 'biblioteca/galeria.html', {'obras': obras})

def cadastrar_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_artistas')
    else:
        form = ArtistaForm()
    return render(request, 'biblioteca/cadastrar.html', {'form': form})

def eventos(request):
    eventos = EventoCultural.objects.all()
    return render(request, 'biblioteca/eventos.html', {'eventos': eventos})

def locais(request):
    locais = LocalArtistico.objects.all()
    return render(request, 'biblioteca/locais.html', {'locais': locais})

def apoio(request):
    apoios = ApoioFinanceiro.objects.all()
    return render(request, 'biblioteca/apoio.html', {'apoios': apoios})

def sobre(request):
    equipe = MembroEquipe.objects.all()
    return render(request, 'biblioteca/sobre.html', {'equipe': equipe})

def contato(request):
    return render(request, 'biblioteca/contato.html')
