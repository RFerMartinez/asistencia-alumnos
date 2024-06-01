from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .forms import ClaseForm
from .models import Clase

# def listar_clases(request):
    
#     ctx = {
#         'clases': Clase.objects.all().order_by("-fecha")
#     }
#     return render(request=request, template_name='clases/lista.html', context=ctx)

class ListarClases(ListView):
    template_name = "clases/lista.html"
    model = Clase
    paginate_by = 15
    context_object_name = "clases"
    
    def get_context_data(self, **kwards):
        ctx = super(ListarClases, self).get_context_data(**kwards)
        ctx['icono'] = "o"
        return ctx
    
    def get_queryset(self):
        return self.model.objects.all().order_by("-fecha")


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

class MisClases(ListView):
    template_name = "clases/mis_clases.html"
    model = Clase
    context_object_name = "clases"
    paginate_by = 15

    def get_queryset(self):
        return self.model.objects.all().order_by("-fecha")