from django.contrib import admin

# Register your models here.

# TODO
from .models import Galeria, Cuadro

admin.site.register(Cuadro)
admin.site.register(Galeria)