from django.shortcuts import render
from .models import Usuario
# Create your views here.
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    """
    print("Todos los usuarios:")
    print(usuarios)
    print(usuarios.query)
    print('Tamaño de los usuarios:',usuarios.count())
    """
    
    ctx = {
        "usuarios": usuarios
    }
    return render(request, 'usuarios/lista.html', ctx)