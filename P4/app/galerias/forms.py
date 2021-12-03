# galerias/forms.py
from django import forms
from .models import *
from django.utils import timezone

class GaleriaForm(forms.ModelForm):
    class Meta:
        model = Galeria
        fields = ('nombre', 'direccion')
    
class CuadroForm(forms.ModelForm):
    class Meta:
        model = Cuadro
        fields = ('nombre', 'galeria', 'autor', 'fecha_creacion', 'imagen')