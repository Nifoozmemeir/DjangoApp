from django import forms

class Curso_Formulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    comision = forms.IntegerField()

class Profesor_Formulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)
    profesion = forms.CharField(max_length=50)

class Estudiante_Formulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)