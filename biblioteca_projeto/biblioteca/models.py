from django.db import models
from django.core.validators import FileExtensionValidator

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome}/{self.uf}"

class EstiloArte(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class ArtistaDeRua(models.Model):
    nome = models.CharField(max_length=100)
    estilo = models.ForeignKey(EstiloArte, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    contato = models.CharField(max_length=100, blank=True)
    redes_sociais = models.CharField(max_length=200, blank=True)
    biografia = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class IntervencaoArtistica(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.ForeignKey(ArtistaDeRua, on_delete=models.CASCADE)
    local = models.CharField(max_length=200)
    data = models.DateField()
    descricao = models.TextField()
    imagem = models.ImageField(
    upload_to='intervencoes/',
    blank=True,
    null=True,
    validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])],
    help_text="Imagem da intervenção (formato JPG ou PNG)"
)
    visivel = models.BooleanField(default=True)


class Intervencao(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField()
    artista = models.ForeignKey('ArtistaDeRua', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class EventoCultural(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField()
    local = models.CharField(max_length=200)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class LocalArtistico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    referencia = models.CharField(max_length=200, blank=True)  # Ex: "Praça Central, perto do museu"

    def __str__(self):
        return self.nome


class ContatoRecebido(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem de {self.nome}"


class ApoioFinanceiro(models.Model):
    tipo = models.CharField(max_length=100)  # Ex: "Pix direto", "Campanha coletiva"
    descricao = models.TextField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.tipo


class MembroEquipe(models.Model):
    nome = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)  # Ex: "Curador", "Desenvolvedor"
    bio = models.TextField(blank=True)
    foto = models.ImageField(upload_to='equipe/', blank=True, null=True)

    def __str__(self):
        return self.nome
