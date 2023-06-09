from django.shortcuts import render
from .models import Person

# Create your views here.



def mostrar_personas(request):
    if request.method == 'POST':
        persons = Person.objects.all()
        return render(request, 'mostrar_personas.html', {'persons': persons})
    
    return render(request, 'mostrar_personas.html')

def hello_world(request):
    
    hello_world = 'Hola a todos, como andan?'
    return render(request, 'hello_world.html', {'hello_world': hello_world})
