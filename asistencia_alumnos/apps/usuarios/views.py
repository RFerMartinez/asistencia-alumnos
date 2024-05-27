from django.shortcuts import render
from apps.usuarios.models import Usuario
from django.views.generic.list import ListView

# Create your views here.
def listar_usuarios(request):
    lista_de_diccionarios_usuarios = Usuario.objects.all() #Aquí es donde se hacen las consultas SQL
    # lista_de_diccionarios_usuarios = Usuario.objects.all().order_by("id")
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

# La infomracion que recibe es un nombre de un template, model
# Las vistas basadas en clases tiene muchos métodos, y se puede redefinir esos métodos
# unos de los métodos necesarios es el que envia informacion via 'context'
# 'ListView' también permite paginar los datos que se muestren
class ListarUsuarios(ListView):
    template_name = "usuarios/listar_todos.html"
    model = Usuario

    # Para paginar los dato que se muestran
    paginate_by = 2

    # Redefinir el nombre del contexto, en vez de que se llame 'object_list', se llamará 'usuarios'
    context_object_name = "usuarios"
    
    #REDEFINIR LA FUNCION PARA MOSTRAR LO DEL CONTEXT
    def get_context_data(self, **kwards):
        # lo siguiente le pide la información que ya tiene en el context, para luego agregar información adicional
        ctx = super(ListarUsuarios, self).get_context_data(**kwards)
        ctx['icono'] = "o"
        # Ahora tiene que retornar el contexto actualizado
        return ctx
    
    def get_queryset(self):
        # Por defecto la consulta que realiza un 'ListView' es un .all() y se lo pasa via 'context'
        # luego en el .html se ocupa lo necesario
        return self.model.objects.all().order_by("pk")