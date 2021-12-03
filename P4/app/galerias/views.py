# galerias/views.py
from django.shortcuts import render, HttpResponse

# Create your views here

def index(request):
    context = {} # Aqui van las variables para la plantilla
    return render(request, 'index.html', context)

# TODO

def ver_cuadro(request):
    return render(request, 'ver_cuadro.html')

def ver_galeria(request):
    return render(request, 'ver_galeria.html')


def crear_cuadro(request):
    if request.method == 'POST':
        # TODO
        pass

    return render(request, 'crear_cuadro.html')

def crear_galeria(request):
    return render(request, 'crear_galeria.html')

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
