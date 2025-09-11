from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artistas/', views.listar_artistas, name='listar_artistas'),
    path('contato/', views.contato, name='contato'),
    path('galeria/', views.galeria, name='galeria'),
    path('cadastrar/', views.cadastrar_artista, name='cadastrar_artista'),
    path('eventos/', views.eventos, name='eventos'),
    path('locais/', views.locais, name='locais'),
    path('sobre/', views.sobre, name='sobre'),
    path('apoio/', views.apoio, name='apoio'),
    path('artista/<int:artista_id>/', views.perfil_artista, name='perfil_artista'),
]
