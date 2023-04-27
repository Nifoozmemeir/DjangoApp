from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.comision}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.email}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    profesion = models.CharField(max_length=50)
    cursos = models.ManyToManyField(Curso)
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.profesion}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nombre} / {self.estudiante}"
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    def __str__(self):
        return f"{self.user} / {self.imagen}"