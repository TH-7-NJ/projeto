from django import forms
from .models import ArtistaDeRua

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = ArtistaDeRua
        fields = ['nome', 'estilo', 'cidade', 'contato', 'redes_sociais', 'biografia']
        widgets = {
            'biografia': forms.Textarea(attrs={'rows': 4}),
        }


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'rows': 4}))
