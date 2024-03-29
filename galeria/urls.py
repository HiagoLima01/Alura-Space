from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path('', index, name=''),
    path('imagem/', imagem, name='imagem')
]