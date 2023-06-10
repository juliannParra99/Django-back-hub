from django.shortcuts import render, redirect
from .models import Person


# Create your views here.

def home(request):
    return render(request, 'home.html')

def mostrar_personas(request):
    persons = Person.objects.create(first_name='John', last_name='Doe')
    persons.foto_perfil = 'C:/Users/julian/Pictures/8a9f828a1371f54eca195e3d31a8d39c.jpg'
    persons.save()
    persons = Person.objects.all()
    return render(request, 'mostrar_personas.html', {'persons': persons})


    

def hello_world(request):
    
    hello_world = 'Hola a todos, como andan?'
    return render(request, 'hello_world.html', {'hello_world': hello_world})
