from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def curso(self, nombre, comision):
    curso = Curso(nombre=nombre, comision=comision)
    curso.save()
    return HttpResponse(f"""
        <p>Curso: {curso.nombre} - Camada: {curso.comision} creado!</p>
        """)

def lista_cursos(self):
    lista = Curso.objects.all()
    return render(self, "lista_cursos.html", {"lista_cursos": lista})

def inicio(self):
    return render(self, "inicio.html")

def cursos(self):
    return render(self, "cursos.html")

def profesores(self):
    return render(self, "profesores.html")

def estudiantes(self):
    return render(self, "estudiantes.html")

def entregables(self):
    return render(self, "entregables.html")

def curso_formulario(request):
    if request.method == 'POST':
        mi_formulario = Curso_Formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            curso = Curso(nombre=request.POST['curso'], comision=request.POST['comision'])
            curso.save()
        return render(request, "inicio.html")
    else:
        mi_formulario = Curso_Formulario()
        return render(request, "curso_formulario.html", {"mi_formulario": mi_formulario})
    
def profesor_formulario(request):
    if request.method == 'POST':
        mi_formulario = Profesor_Formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            profesor = Profesor(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'], profesion=request.POST['profesion'])
            profesor.save()
        return render(request, "inicio.html")
    else:
        mi_formulario = Profesor_Formulario()
        return render(request, "profesores_formulario.html", {"mi_formulario": mi_formulario})
    
def estudiante_formulario(request):
    if request.method == 'POST':
        mi_formulario = Estudiante_Formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            estudiante = Estudiante(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'])
            estudiante.save()
        return render(request, "inicio.html")
    else:
        mi_formulario = Estudiante_Formulario()
        return render(request, "estudiante_formulario.html", {"mi_formulario": mi_formulario})
    
def busqueda_comision(request):
    return render(request, "busqueda_comision.html")

def buscar(request):
    if request.GET["comision"]:
        comision = request.GET["comision"]
        cursos = Curso.objects.filter(comision=comision)
        return render(request, "resultados_busqueda.html", {"cursos": cursos, "comision": comision})
    else:
        return HttpResponse("No enviaste info")