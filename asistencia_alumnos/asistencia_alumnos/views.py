'''
Al momento de escribir vistas, existen dos tipos de vistas. Vistas basadas en funciones y vistas basadas en clases
estas son dos formas de escribir un controlador
'''

from django.shortcuts import render

# VISTA  A PARTIR DE UNA FUNCION
# el protocolo http que permite comunicar entre cliente y servidor son solicitudes y respuestas
# por ende, en la funcion voy a recibir una solicitud
def login(request):
    # paar renderizar 
    return render(request=request, template_name='login.html', context={})

def home(request):
    lista_de_diccionarios_alumnos = [
        {
            'nombre': 'Federico',
            'apellido': 'Aguirre',
            'legajo': 222,
            'habilitado': True,
        },
        {
            'nombre': 'Fernando',
            'apellido': 'Martínez',
            'legajo': 13333,
            'habilitado': False,
        },
        {
            'nombre': 'Franco',
            'apellido': 'Lopez',
            'legajo': 9852,
            'habilitado': True,
        }
    ]
    ctx = {
        'alumnos': lista_de_diccionarios_alumnos,
    }
    return render(request=request, template_name='home.html', context=ctx)

