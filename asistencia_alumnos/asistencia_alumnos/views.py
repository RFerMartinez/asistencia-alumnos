'''
Al momento de escribir vistas, existen dos tipos de vistas. Vistas basadas en funciones y vistas basadas en clases
estas son dos formas de escribir un controlador
'''

from django.shortcuts import render

from apps.usuarios.models import Usuario

# VISTA  A PARTIR DE UNA FUNCION
# el protocolo http que permite comunicar entre cliente y servidor son solicitudes y respuestas
# por ende, en la funcion voy a recibir una solicitud
def login(request):
    # paar renderizar 
    return render(request=request, template_name='login.html', context={})

def home(request):

    ctx = {
    }
    return render(request=request, template_name='home.html', context=ctx)

