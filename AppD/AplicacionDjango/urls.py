from django.contrib import admin
from django.urls import path
from AplicacionDjango.views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-cursos', lista_cursos),
    path('', inicio, name="Inicio"),
    path('cursos', cursos, name="Cursos"),
    path('profes', profesores, name="Profesores"),
    path('est', estudiantes, name="Estudiantes"),
    path('entregables', entregables, name="Entregables"),
    path('curso-form', curso_formulario, name="CursoFormulario"),
    path('profes-form', profesor_formulario, name="ProfesoresFormulario"),
    path('est-form', estudiante_formulario, name="EstudiantesFormulario"),
    path('busq-com', busqueda_comision, name="BusquedaComision"),
    path('buscar', buscar, name="Buscar"),
]