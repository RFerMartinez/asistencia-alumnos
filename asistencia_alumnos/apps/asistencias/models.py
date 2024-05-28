from django.db import models

from apps.clases.models import Clase
from apps.usuarios.models import Usuario

'''
on_delete=models.CASCEDE()

'''

class Asistencia(models.Model):
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
