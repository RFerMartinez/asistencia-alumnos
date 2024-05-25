from django.urls import path
from . import views

app_name = "clases"


urlpatterns = [
    path('listar-todos/', views.listar_clases, name='listar_clases'),
    path('nueva/', views.CrearClase.as_view(), name='crear'),
]
'''
La url se va a dirigir a 'listar-todos' (similar a listar para los alumnos), pero va a llamar a una vista diferente.
el 'name='listar_clases'' se lo puede utilizar para referenciar en los templates
.......USO DEL name='listar_clases........
<a href="{% url 'clases:listar_clases' %}">Ver todos las clases</a>
'''

