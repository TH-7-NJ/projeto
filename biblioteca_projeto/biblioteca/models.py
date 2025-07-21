from django.db import models

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
    imagem = models.URLField(blank=True, help_text="Link para imagem da intervenção")
    visivel = models.BooleanField(default=True)


class Intervencao(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField()
    artista = models.ForeignKey('ArtistaDeRua', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    def __str__(self):
        return self.titulo
