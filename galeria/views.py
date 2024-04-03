from django.shortcuts import render, get_object_or_404

from galeria.models import Fotografia

def index(request):
    """
    Função para renderização da página index

    """

    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicado=True)

    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    """
    Função para renderização da página index

    """
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    """
    Função para renderização da página index

    """
    
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicado=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/buscar.html", {"cards": fotografias})