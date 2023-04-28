from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import *

class Curso_Formulario(forms.ModelForm):
    class Meta:
        model=Curso
        fields=('__all__')

class Profesor_Formulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)
    profesion = forms.CharField(max_length=50)

class Estudiante_Formulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)

class UsuarioEditForm(UserChangeForm):
    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('first_name', 'last_name', 'email', 'password1', 'password2')
    def clean_password2(self):
        print(self.cleaned_data)
        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden!")
        return password2
    
class Avatar_Formulario(forms.ModelForm):
    class Meta:
        model=Avatar
        fields = ['imagen']