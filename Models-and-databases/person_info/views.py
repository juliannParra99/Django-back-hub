from django.shortcuts import render
from .models import Person

# Create your views here.


#  persons es un QuerySet de objetos Person que se obtiene mediante la llamada a Person.objects.all(). Un QuerySet es esencialmente una lista de objetos que se pueden iterar y acceder a través de un bucle for en una plantilla Django.


# Esta funcion no es muy practica por que cada que se recarga la pagina se vuelve a ejecutar y vuelve a isntanciar el objeto, por lo que van a aparecer nombre repetidos.
def mostrar_personas(request):
    person1 = Person(first_name='John', last_name='Doe')
    person2 = Person(first_name='Jane', last_name='Smith')
    
    # Guardar las instancias en la base de datos
    person1.save()
    person2.save()
    
    # TEMA: QUERYSET
    # Recuperar todos los objetos Person de la base de datos (los que usaron la funcion save())
    #  devuelve un QuerySet que representa TODOS los objetos Person 
    persons = Person.objects.all()
    
    return render(request, 'mostrar_personas.html', {'persons': persons})

def hello_world(request):
    
    hello_world = 'Hola a todos, como andan?'
    return render(request, 'hello_world.html', {'hello_world': hello_world})
