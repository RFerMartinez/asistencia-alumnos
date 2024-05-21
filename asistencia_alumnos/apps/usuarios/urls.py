from django.urls import path
from . import views

app_name = "usuarios"
'''
Lo anterior se hace ya que puede haber varias urls que se dirigan a 'listar-todos', puede ser 'listar-todos' de
materias, de alumnos, etc. Para ello se le da un nombre un nombre 'app_name= "usuarios"'
'''

urlpatterns = [
    path('listar-todos/', views.listar_usuarios, name='listar_todos'),
]