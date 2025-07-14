from django.urls import path
from .views import index, cadastrar_artista

urlpatterns = [
    path('', index, name='index'),
    path('cadastrar/', cadastrar_artista, name='cadastrar_artista'),
]
