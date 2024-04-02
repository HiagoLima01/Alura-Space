from django.urls import path
from galeria.views import index, imagem, buscar

urlpatterns = [
    path('', index, name=''),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar')
]