from django.contrib import admin
from django.urls import path
from AplicacionDjango.views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-cursos', lista_cursos),
    path('', inicio),
    path('cursos', cursos),
    path('prof', profesores),
    path('est', estudiantes),
    path('entregables', entregables),
]