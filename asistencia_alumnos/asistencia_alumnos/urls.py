
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('login/', views.login),
]

# Siempre que definimos una URL lo va a manejar un controlador, en caso de Django es una vista.
# MVT
# Para esto se definió un nuevo archivo views.py

