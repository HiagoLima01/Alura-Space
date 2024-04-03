from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):

    """
    Classe para melhorar ferramenta de upload e visualização no Admin  

    """

    list_display = ('id', 'nome', 'legenda', 'publicado')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_filter = ('categoria',)
    list_editable = ('publicado',)
    list_per_page = 10

# Método para aplicar a classe fotografia no Admin e melhorias na forma de upload
admin.site.register(Fotografia, ListandoFotografias)
