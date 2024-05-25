from django.db import models

class Clase(models.Model):
    fecha = models.DateField()


'''
Lo siguiente es para darle un nombre a la tabla, en vez del nombre que crea Django por defecto

Djando crea una tabla de migraciones, para verificar las migraciones que se hicieron

class NuevaTabla(models.Model):
    pass

    class Meta:
        db_table = 'nueba_tabla'

'''