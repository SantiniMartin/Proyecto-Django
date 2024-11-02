from django.shortcuts import render

# Create your views here.
def lista_usuarios(request):
    return render(request, 'lista_usuarios.html', {})