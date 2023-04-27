from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('l-cursos', lista_cursos),
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
    path('l-profes', lista_profesores, name="ListaProfesores"),
    path('e-profes/<int:id>', eliminar_profesor, name="EliminarProfesor"),
    path('ed-profes/<int:id>', editar_profesor, name="EditarProfesor"),
    path('lv-cursos', CursoList.as_view(), name="CursosListView"),
    path('detv-cursos/<pk>', CursoDetail.as_view(), name="CursosDetailView"),
    path('cv-cursos', CursoCreate.as_view(), name="CursosCreateView"),
    path('up-cursos/<pk>', CursoUpdate.as_view(), name="CursosUpdateView"),
    path('delv-cursos/<pk>', CursoDelete.as_view(), name="CursosDeleteView"),
    path('login', login_usuarios, name="Login"),
    path('reg-usu', registro_usuarios, name="RegistroUsuarios"),
    path('logout', LogoutView.as_view(template_name='logout.html'), name="Logout"),
    path('ed-perfil', editar_perfil, name="EditarPerfil"),
]