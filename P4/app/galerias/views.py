# galerias/views.py
from django.shortcuts import render, HttpResponse

# Create your views here

def index(request):
    return HttpResponse('Hello World!')

def test_template(request):
    context = {} # Aqui van las variables para la plantilla
    return render(request, 'test.html', context)

# TODO

def crear_cuadro(request):
    pass

def crear_galeria(request):
    pass

def aniadir_cuadro(request):
    pass

def aniadir_galeria(request):
    pass

def borrar_cuadro(request):
    pass

def borrar_galeria(request):
    pass

def modificar_cuadro(request):
    pass

def modificar_galeria(request):
    pass