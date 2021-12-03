# galerias/views.py
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *

# Create your views here

def index(request):
    context = {} # Aqui van las variables para la plantilla
    return render(request, 'index.html', context)

# TODO

def ver_cuadro(request):
    cuadros = Cuadro.objects.all()

    return render(request, 'ver_cuadro.html', {"cuadros":cuadros})

def ver_galeria(request):
    galerias = Galeria.object.all()
    
    return render(request, 'ver_galeria.html')

def crear_cuadro(request):
    if request.method == 'POST':
        form = CuadroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('ver_cuadro')
    else:
        form = CuadroForm()

    return render(request, 'crear_cuadro.html', {"form":form})

def crear_galeria(request):
    if request.method == 'POST':
        form = GaleriaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('ver_cuadro')
    else:
        form = GaleriaForm()

    return render(request, 'crear_galeria.html', {"form":form})

def aniadir_cuadro(request):
    return render(request, 'aniadir_cuadro.html')


def aniadir_galeria(request):
    return render(request, 'aniadir_galeria.html')


def borrar_cuadro(request):
    pass

def borrar_galeria(request):
    pass

def modificar_cuadro(request):
    return render(request, 'modificar_cuadro.html')


def modificar_galeria(request):
    return render(request, 'modificar_galeria.html')
