from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .forms import FormPaciente
from .models import Paciente

# Create your views here.
# def lista(request):
    
#     template_name = 'pacientes/lista.html'
    
#     return render(request, template_name)

class Lista(ListView):
    template_name = 'pacientes/lista.html'
    model = Paciente
    context_object_name = 'pacientes'
    paginate_by = 2
    
    def get_queryset(self):
        return self.model.objects.all().order_by('nombre') #.filter(nombre='Antonela')


class Nuevo(CreateView):
    template_name = 'pacientes/nuevo.html'
    model = Paciente
    form_class = FormPaciente
    success_url = reverse_lazy('pacientes:lista')
    
    def get_context_data(self, **kwargs):
        ctx = super(Nuevo, self).get_context_data(**kwargs)
        ctx['titulo'] = 'Nuevo Paciente'
        print("Hola estoy en el get context")
        return ctx
    
"""
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
"""