from django.shortcuts import render, redirect
from .forms import FormPaciente

# Create your views here.
def lista(request):
    
    template_name = 'pacientes/lista.html'
    
    return render(request, template_name)

def nuevo(request):
    
    template_name = 'pacientes/nuevo.html'
    # form = FormUsuario()
    form = FormPaciente()
    message = '' 
    if request.method == "POST":
        form = FormPaciente(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('pacientes:lista')
        else:
            message = 'No se pudo guardar de forma correcta el formulario.'
        
    ctx = {
        'form': form,
        'message': message
    }
    
    return render(request, template_name, ctx)