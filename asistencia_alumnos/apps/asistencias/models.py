from django.db import models

from apps.clases.models import Clase
from apps.usuarios.models import Usuario

'''
on_delete=models.CASCEDE()

'''

class Asistencia(models.Model):
    # Con esta tabla se puede saber que usuario estubo presente el que clase...
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mis_asistencias')
    # Con el nombre de la relacion anterior, "yo parado en un usuario, al ahcer en 'mis_asistencias', me va a devolver todas
    # las asistencias para el usuario en el que estoy parado"

    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name="asistencias_relacion")
