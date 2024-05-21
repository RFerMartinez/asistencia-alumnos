from django.contrib.auth.models import AbstractUser #Esto se ahce para trabajar con la abla 'users' que ya trae Django

from django.db import models

class Usuario(AbstractUser):
    biografia = models.CharField(max_length=255, null=True, blank=True)
    # Lo anterior se tiene que actualizar en una tabla 'Usuario' ya existente
    # para esto, se crea un script en python con el comando 'makemigrations'. Esto luego se convierte en un sql

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, ({self.username})"

