'''
Al momento de escribir vistas, existen dos tipos de vistas. Vistas basadas en funciones y vistas basadas en clases
estas son dos formas de escribir un controlador
'''

from django.shortcuts import render, redirect

from apps.usuarios.models import Usuario
from apps.usuarios.forms import FormularioRegistro, FormularioRegistroUsuario

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

def registrarme(request):
    template_name = "registrarme.html"
    form = FormularioRegistroUsuario()

    mensajeTodoCorrecto = None

    if request.method == 'POST':
        # Guardar el usuario. FORMA ARTESANAL
        '''
        usernameObtenido = request.POST.get('username')
        last_nameObtenido = request.POST.get('last_name')
        first_nameeObtenido = request.POST.get('first_name')
        passwordObtenido = request.POST.get('password')
        print(f"username --> {usernameObtenido}\nlast_name --> {last_nameObtenido}\nfirst_name --> {first_nameeObtenido}\npassword --> {passwordObtenido}")
        
        u = Usuario(
            username = usernameObtenido,
            last_name = last_nameObtenido,
            first_name = first_nameeObtenido,
            password = passwordObtenido,
        )
        # Debido a que Usuario hereda de AbstracUser, tiene un método que hereda, es el método save()
        u.save()
        '''
        form = FormularioRegistroUsuario(request.POST)
        print(f"is_valid: {form.is_valid()}")

        if form.is_valid():
            form.save()
            mensajeTodoCorrecto = "Usuario creado correctamente, puede iniciar sesion"
        else:
            print(f"ERRORES: {form.errors}")

    ctx = {
        'form': form,
        'mensajeTodoCorrecto': mensajeTodoCorrecto,
    }
    return render(request=request, template_name=template_name, context=ctx)

