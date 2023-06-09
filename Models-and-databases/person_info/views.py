from django.shortcuts import render, redirect
from .models import Person


# Create your views here.

def home(request):
    return render(request, 'home.html')

def mostrar_personas(request):
    persons = Person.objects.all()
    return render(request, 'mostrar_personas.html', {'persons': persons})


    

def hello_world(request):
    
    hello_world = 'Hola a todos, como andan?'
    return render(request, 'hello_world.html', {'hello_world': hello_world})
