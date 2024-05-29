from django.urls import path

from . import views

app_name = "materias"

urlpatterns = [
    path('listar/', views.Listar.as_view(), name='listar_materias'),
    path('nuevo/', views.CrearMateria.as_view(), name='nuevo'),
]