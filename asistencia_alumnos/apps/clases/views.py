from django.shortcuts import render
from apps.usuarios.models import Usuario

# Create your views here.
def listar_clases(request):
    
    ctx = {
    }
    return render(request=request, template_name='clases/lista.html', context=ctx)
