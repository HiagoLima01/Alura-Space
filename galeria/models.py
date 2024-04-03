from django.db import models
from datetime import datetime

class Fotografia(models.Model):
    """
    Classe para representar a relação de Fotografia no banco de dados

    Atributos:

        nome:str                      Nome da foto
        legenda:str                   Legenda da foto
        OPCOES_CATEGORIA:boolean      Lista com as possiveis categorias presentes no site
        categoria;str                 Categoria da foto
        descricao:str                 Descricao da foto
        foto:srt                      Campo para upload de fotos
        publicado:boolean             Campo boleano para definir se uma foto é publicada ou não
        data_fotografia:datetima      Coleta a data do momento do post
    
    Métodos:

        
    
    """

    OPCOES_CATEGORIA = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALÁXIA', 'Galáxia'),
        ('PLANETA', 'Planeta'),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices= OPCOES_CATEGORIA, default= '')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicado = models.BooleanField(default=False)
    data_fotografia = models.DateField(default=datetime.now, blank = False)

    def __str__(self):
        return self.nome