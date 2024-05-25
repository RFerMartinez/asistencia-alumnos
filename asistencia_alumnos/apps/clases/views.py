from django.shortcuts import render
from apps.usuarios.models import Usuario
from .models import Clase

# Create your views here.
def listar_clases(request):
    
    ctx = {
        'clases': Clase.objects.all().order_by("fecha")
    }
    return render(request=request, template_name='clases/lista.html', context=ctx)
