# galerias/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),

    # mostrar
    path('ver_cuadro', views.ver_cuadro, name="ver_cuadro"),
    path('ver_galeria', views.ver_galeria, name="ver_galeria"),
    # crear
    path('crear_cuadro', views.crear_cuadro, name="crear_cuadro"),
    path('crear_galeria', views.crear_galeria, name="crear_galeria"),
    # borrar
    path('borrar_cuadro/<int:n>', views.borrar_cuadro, name="borrar_cuadro"),
    path('borrar_galeria/<int:n>', views.borrar_galeria, name="borrar_galeria"),
    # modificar
    path('modificar_cuadro/<int:n>', views.modificar_cuadro, name="modificar_cuadro"),
    path('modificar_galeria/<int:n>', views.modificar_galeria, name="modificar_galeria"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)