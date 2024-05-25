from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

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

