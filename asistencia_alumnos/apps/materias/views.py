from django.views.generic.list import ListView

from .models import Materia

class ListarClases(ListView):
    template_name = "materias/listar.html"
    model = Materia
    paginate_by = 10
    context_object_name = "materias"
    
    def get_queryset(self):
        return self.model.objects.all()

