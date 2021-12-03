# galerias/forms.py
from django import forms
from .models import Cuadro
from django.utils import timezone

class GaleriaForm(forms.Form):
    nombre = forms.CharField(max_length=200)
    direccion = forms.CharField(max_length=100)
    # ...
    
class CuadroForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    #galeria = forms.ForeignKey(Galeria, on_delete=forms.CASCADE)
    autor = forms.CharField(max_length=100)
    fecha_creacion = forms.DateField(default=timezone.now)
    # ...
    imagen = forms.ImageField(upload_to='img/', default='img/default.jpg') # imagen del cuadro

# TODO ?
# no se si hacen falta mas clases o modificarlas