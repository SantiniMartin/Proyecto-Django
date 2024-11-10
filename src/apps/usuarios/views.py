from django.shortcuts import render, redirect
from .models import Usuario
from .forms import FormUsuario, FormUser

# Create your views here.
def nuevo(request):
    
    template_name = 'usuarios/nuevo.html'
    # form = FormUsuario()
    form = FormUser()
    message = '' 
    if request.method == "POST":
        form = FormUser(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('usuarios:lista')
        else:
            message = 'No se pudo guardar de forma correcta el formulario.'
        
    ctx = {
        'form': form,
        'message': message
    }
    
    return render(request, template_name, ctx)

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