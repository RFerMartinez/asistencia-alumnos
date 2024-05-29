from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import MateriaForm
from .models import Materia

class Listar(ListView):
    template_name = "materias/listar.html"
    model = Materia
    paginate_by = 10
    context_object_name = "materias"
    
    def get_queryset(self):
        return self.model.objects.all()


class CrearMateria(CreateView):
    template_name = "materias/crear.html"
    model = Materia
    form_class = MateriaForm
    success_url = reverse_lazy('clases:listar_clases')