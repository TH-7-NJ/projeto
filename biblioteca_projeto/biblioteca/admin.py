from django.contrib import admin
from .models import Cidade, EstiloArte, ArtistaDeRua, IntervencaoArtistica

admin.site.register(Cidade)
admin.site.register(EstiloArte)
admin.site.register(ArtistaDeRua)
admin.site.register(IntervencaoArtistica)
