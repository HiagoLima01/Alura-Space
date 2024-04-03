from django.urls import path
from usuarios.views import login, cadastro


urlpatterns = [
    path('usuario/login', login, name='login'),
    path('usuario/cadastro', cadastro, name='cadastro'),
    


]