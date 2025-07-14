from django import forms
from .models import ArtistaDeRua

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = ArtistaDeRua
        fields = ['nome', 'estilo', 'cidade', 'contato', 'redes_sociais', 'biografia']
        widgets = {
            'biografia': forms.Textarea(attrs={'rows': 4}),
        }
