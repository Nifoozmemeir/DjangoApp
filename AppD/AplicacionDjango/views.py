from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
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
            return HttpResponseRedirect('/Appdjango/')
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
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
            return HttpResponseRedirect('/Appdjango/')
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
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
            return HttpResponseRedirect('/Appdjango/')
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
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

@login_required
@staff_member_required(login_url='/Appdjango/')
def lista_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, "leer_profesores.html", {"profesores": profesores})

def eliminar_profesor(request, id):
    if request.method == 'POST':
        profesor = Profesor.objects.get(id=id)
        profesor.delete()
        profesores = Profesor.objects.all()
        return render(request, "leer_profesores.html", {"profesores": profesores})
    
def editar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    if request.method == 'POST':
        mi_formulario = Profesor_Formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            profesor.nombre = data['nombre']
            profesor.apellido = data['apellido']
            profesor.email = data['email']
            profesor.profesion = data['profesion']
            profesor.save()
            return HttpResponseRedirect('/Appdjango/')
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
        mi_formulario = Profesor_Formulario(initial={
            "nombre": profesor.nombre,
            "apellido": profesor.apellido,
            "email": profesor.email,
            "profesion": profesor.profesion
        })
        return render(request, "editar_profesor.html", {"mi_formulario": mi_formulario, "id": profesor.id})
    
class CursoList(LoginRequiredMixin, ListView):
    model = Curso
    template_name = "curso_list_view.html"
    context_object_name = "cursos"

class CursoDetail(DetailView):
    model = Curso
    template_name = "curso_detail_view.html"
    context_object_name = "curso"

class CursoCreate(CreateView):
    model = Curso
    template_name = "curso_create_view.html"
    fields = ['nombre', 'comision']
    success_url = '/Appdjango/'

class CursoUpdate(UpdateView):
    model = Curso
    template_name = "curso_update_view.html"
    fields = ('__all__')
    success_url = '/Appdjango/'
    context_object_name = 'curso'

class CursoDelete(DeleteView):
    model = Curso
    template_name = "curso_delete_view.html"
    success_url = '/Appdjango/'

def login_usuarios(request):
    if request.method == 'POST':
        mi_formulario = AuthenticationForm(request, data=request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            usuario = data["username"]
            contraseña = data["password"]
            user = authenticate(username=usuario, password=contraseña)
            if user:
                login(request, user)
                return render(request, 'inicio.html', {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, 'inicio.html', {"mensaje": "Error: datos incorrectos"})
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
        mi_formulario = AuthenticationForm()
        return render(request, "login.html", {"mi_formulario": mi_formulario})
    
def registro_usuarios(request):
    if request.method == 'POST':
        mi_formulario = UserCreationForm(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            username = data["username"]
            mi_formulario.save()
            return render(request, 'inicio.html', {"mensaje": f"Usuario {username} creado!"})
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
        mi_formulario = UserCreationForm()
        return render(request, "registro_usuarios.html", {"mi_formulario": mi_formulario})