from django.shortcuts import render
from apps.usuarios.models import Usuario

# Create your views here.
def listar_usuarios(request):
    lista_de_diccionarios_usuarios = Usuario.objects.all() #Aquí es donde se hacen las consultas SQL
    # lista_de_diccionarios_usuarios = Usuario.objects.filter(is_superuser=True)

    # print("========================================")
    # print(lista_de_diccionarios_usuarios) 
    # print("iterando usuarios")
    # for us in lista_de_diccionarios_usuarios:
    #     print("Usuario: ", us)

    # print("-------- CONSULTA QUERY----------")
    # print("Query: ", lista_de_diccionarios_usuarios.query)
    # print("========================================")

    ctx = {
        'usuarios': lista_de_diccionarios_usuarios,
    }
    return render(request=request, template_name='usuarios/listar_todos.html', context=ctx)