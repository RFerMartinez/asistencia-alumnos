'''
Al momento de escribir vistas, existen dos tipos de vistas. Vistas basadas en funciones y vistas basadas en clases
estas son dos formas de escribir un controlador
'''

from django.shortcuts import render, redirect

from apps.usuarios.models import Usuario

from django.contrib.auth import authenticate, login as login_django

# VISTA  A PARTIR DE UNA FUNCION
# el protocolo http que permite comunicar entre cliente y servidor son solicitudes y respuestas
# por ende, en la funcion voy a recibir una solicitud
def login(request):
    
    print("================================================")
    # print(request.POST)

    nombreUsuaio = ""
    mensajeError = None
    if request.method == 'POST':
        nombreUsuaio=request.POST.get('username')
        contrasenia=request.POST.get('password')

        objeto = authenticate(request=request, username=nombreUsuaio, password=contrasenia)

        if objeto:
            login_django(request, objeto)
            # Si se loguea, se lo lleva a la pagina de home
            return redirect('pagina_principal')

            # print("Inicio se secion correcto.")
        else:
            mensajeError = "Usuario y/o contraseña incorrecta"

        print(f"---> {objeto}")

        # objeto = Usuario.objects.filter(username=nombreUsuaio).first() # Me recupera (filtra) el objeto que coincida con el 'username'en la DB
        # print(f"----> {objeto.password}")
        # print(f"----> {contrasenia}")

        # print(f"Usuario: {nombreUsuaio} - Contraseña: {contrasenia}")

    # print("request método -->", request.method)
    print("================================================")

    # Para que quede guardado el 'username' en el formulario
    ctx = {
        "nombre_usuario": nombreUsuaio,
        "mensaje_error": mensajeError
    }

    return render(request=request, template_name='login.html', context=ctx)

def home(request):

    ctx = {
    }
    return render(request=request, template_name='home.html', context=ctx)

