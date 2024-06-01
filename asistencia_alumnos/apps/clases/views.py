from django.http.response import HttpResponse as HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.utils.mixins import VerificarPermisos

from .forms import ClaseForm
from .models import Clase

# def listar_clases(request):
    
#     ctx = {
#         'clases': Clase.objects.all().order_by("-fecha")
#     }
#     return render(request=request, template_name='clases/lista.html', context=ctx)

# Hay una funcion que tiene todas las vistas basadas en clases, es la funcion distpach
# es una funcion que se ejecuta antes que todo
class ListarClases(LoginRequiredMixin, VerificarPermisos, ListView):
    template_name = "clases/lista.html"
    model = Clase
    paginate_by = 15
    context_object_name = "clases"
    
    def get_context_data(self, **kwards):
        # print("Estoy en el get_context_data de listar clases")
        ctx = super(ListarClases, self).get_context_data(**kwards)
        ctx['icono'] = "o"
        return ctx
    
    def get_queryset(self):
        # print("Estoy en el get_queryset de listar clases")
        return self.model.objects.all().order_by("-fecha")

class CrearClase(LoginRequiredMixin, VerificarPermisos, CreateView):
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