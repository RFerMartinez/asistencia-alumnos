from django.contrib import admin

from .models import Categoria, Materia

# Para customizar la vista que se ve desde la url de /admin
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre"]

admin.site.register(Categoria, CategoriaAdmin)

class MateriaAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre"]

admin.site.register(Materia, MateriaAdmin)
