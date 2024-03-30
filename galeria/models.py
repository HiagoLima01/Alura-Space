from django.db import models

class Fotografia(models.model):
    nome = models.CharField(max_Length=100, null=False, blank=False)
    legends = models.CharField(max_Length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_Length=100, null=False, blank=False)
