# galerias/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('test_template', views.test_template, name="test_template"),
    # crear
    #path('crear_cuadro', views.crear_cuadro, name="crear_cuadro"),
    #path('crear_galeria', views.crear_galeria, name="crear_galeria"),
    # añadir
    #path('aniadir_cuadro', views.aniadir_cuadro, name="añadir_cuadro"),
    #path('aniadir_galeria', views.aniadir_galeria, name="añadir_galeria"),
    # borrar
    #path('borrar_cuadro', views.borrar_cuadro, name="borrar_cuadro"),
    #path('borrar_galeria', views.borrar_galeria, name="borrar_galeria"),
    # modificar
    #path('modificar_cuadro', views.modificar_cuadro, name="modificar_cuadro"),
    #path('modificar_galeria', views.modificar_galeria, name="modificar_galeria"),
]

# TODO