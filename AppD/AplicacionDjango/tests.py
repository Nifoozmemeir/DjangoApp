from django.test import TestCase
from django.urls import reverse
from .models import *
from .forms import *
from .views import *

# Create your tests here.

class ProfesorFormularioTestCase(TestCase):
    def test_profesor_formulario(self):
        # Simula una solicitud POST con datos válidos
        response = self.client.post('/profesor-formulario/', {'nombre': 'Juan', 'apellido': 'Perez', 'email': 'juan@example.com', 'profesion': 'Ingeniero'})
        print(f"RESPONSE: {response}")
        print(f"RESPONSE STATUS CODE: {response.status_code}")
        print(f"RESPONSE URL: {response.url}")
        print(f"RESPONSE CONTENT: {response.content}")
        
        # Verifica que la respuesta redirija a la página principal
        self.assertRedirects(response, '/Appdjango/')

        # Verifica que el objeto Profesor haya sido creado en la base de datos
        from .models import Profesor
        profesor = Profesor.objects.get(nombre='Juan', apellido='Perez', email='juan@example.com', profesion='Ingeniero')
        self.assertEqual(profesor.nombre, 'Juan')
        self.assertEqual(profesor.apellido, 'Perez')
        self.assertEqual(profesor.email, 'juan@example.com')
        self.assertEqual(profesor.profesion, 'Ingeniero')

        # Simula una solicitud POST con datos inválidos
        response = self.client.post('/profesor-formulario/', {'nombre': '', 'apellido': '', 'email': '', 'profesion': ''})

        # Verifica que la respuesta renderice el template 'inicio.html'
        self.assertTemplateUsed(response, 'inicio.html')

        # Verifica que se muestre el mensaje de error en el template
        self.assertContains(response, 'Formulario invalido')
