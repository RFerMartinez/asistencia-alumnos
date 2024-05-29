from django.urls import path

from . import views

app_name = "materias"

urlpatterns = [
    path('listar/', views.ListarClases.as_view(), name='listar_materias'),
]