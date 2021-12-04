# galerias/views.py
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *

# Create your views here

def index(request):
    context = {} # Aqui van las variables para la plantilla
    return render(request, 'index.html', context)

def ver_cuadro(request):
    cuadros = Cuadro.objects.all()

    return render(request, 'ver_cuadro.html', {"cuadros":cuadros})

def ver_galeria(request):
    galerias = Galeria.objects.all()
    
    return render(request, 'ver_galeria.html', {"galerias":galerias})

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
            return redirect('ver_galeria')
    else:
        form = GaleriaForm()

    return render(request, 'crear_galeria.html', {"form":form})

def aniadir_cuadro(request, n):
    # TODO
    pass

def aniadir_galeria(request):
    # TODO
    pass


def borrar_cuadro(request, n):
    c = Cuadro.objects.get(id=n)
    c.delete()

    return redirect('ver_cuadro')

def borrar_galeria(request, n):
    g = Galeria.objects.get(id=n)
    g.delete()

    return redirect('ver_galeria')

def modificar_cuadro(request, n):
    c = Cuadro.objects.get(id=n)
    form = CuadroForm(instance=c)

    if request.method == 'POST':
        form = CuadroForm(request.POST, instance=c)

        if form.is_valid():
            form.save()
            
            return redirect('ver_cuadro')

    return render(request, 'modificar_cuadro.html', {"form":form, "n":n})


def modificar_galeria(request, n):
    g = Galeria.objects.get(id=n)
    form = GaleriaForm(instance=g)

    if request.method == 'POST':
        form = GaleriaForm(request.POST, instance=g)

        if form.is_valid():
            form.save()
            
            return redirect('ver_galeria')

    return render(request, 'modificar_galeria.html', {"form":form, "n":n})
