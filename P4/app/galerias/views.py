# galerias/views.py
from django.shortcuts import render, HttpResponse

# Create your views here

def index(request):
    return HttpResponse('Hello World!')

def test_template(request):
    context = {} # Aqui van las variables para la plantilla
    return render(request, 'test.html', context)
