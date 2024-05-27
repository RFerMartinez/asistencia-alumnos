from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from .forms import ClaseForm
from .models import Clase

# Create your views here.
def listar_clases(request):
    
    ctx = {
        'clases': Clase.objects.all().order_by("-fecha")
    }
    return render(request=request, template_name='clases/lista.html', context=ctx)


class CrearClase(CreateView):
    template_name = "clases/crear.html"
    model = Clase
    form_class = ClaseForm
    success_url = reverse_lazy('clases:listar_clases')

class EditarClase(UpdateView):
    template_name = "clases/editar.html"
    model = Clase
    form_class = ClaseForm #Tiene el mismo modelo, ya que los campos que se usan para crear, también se usan para editar
    success_url = reverse_lazy('clases:listar_clases')
