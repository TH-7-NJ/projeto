from django.contrib import admin
from .models import ArtistaDeRua, IntervencaoArtistica, Cidade, EstiloArte

@admin.register(ArtistaDeRua)
class ArtistaDeRuaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estilo', 'cidade')
    search_fields = ('nome', 'cidade__nome', 'estilo__nome')
    list_filter = ('estilo', 'cidade')

@admin.register(IntervencaoArtistica)
class IntervencaoArtisticaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'artista', 'local', 'visivel')
    search_fields = ('titulo', 'artista__nome', 'local')
    list_filter = ('visivel', 'data')

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'uf')
    search_fields = ('nome',)

@admin.register(EstiloArte)
class EstiloArteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
from .models import Intervencao

@admin.register(Intervencao)
class IntervencaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'artista', 'data')
    search_fields = ('titulo', 'descricao', 'artista__nome')
    list_filter = ('data',)

from .models import EventoCultural, LocalArtistico, ContatoRecebido, ApoioFinanceiro, MembroEquipe

@admin.register(EventoCultural)
class EventoCulturalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'local', 'cidade')
    search_fields = ('nome', 'descricao', 'local')
    list_filter = ('cidade', 'data')

@admin.register(LocalArtistico)
class LocalArtisticoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'referencia')
    search_fields = ('nome', 'referencia')
    list_filter = ('cidade',)

@admin.register(ContatoRecebido)
class ContatoRecebidoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_envio')
    search_fields = ('nome', 'email', 'mensagem')
    readonly_fields = ('data_envio',)

@admin.register(ApoioFinanceiro)
class ApoioFinanceiroAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'link')
    search_fields = ('tipo', 'descricao')

@admin.register(MembroEquipe)
class MembroEquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'funcao')
    search_fields = ('nome', 'funcao', 'bio')
