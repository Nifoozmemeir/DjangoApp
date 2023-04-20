from django.contrib import admin
from django.urls import path
from AplicacionDjango.views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-cursos', lista_cursos),
    path('', inicio, name="Inicio"),
    path('cursos', cursos, name="Cursos"),
    path('prof', profesores, name="Profesores"),
    path('est', estudiantes, name="Estudiantes"),
    path('entregables', entregables, name="Entregables"),
]