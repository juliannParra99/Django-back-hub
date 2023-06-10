from django.db import models

# Create your models here.
class Person(models.Model):
    # En este código, se ha agregado el campo id como un AutoField con el parámetro primary_key=True. Esto hará que Django genere automáticamente valores numéricos únicos para el campo id al momento de guardar cada objeto Person en la base de datos.   Si se quiere que la primary key sea un string se puede usar el charField()
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # El campo ImageField es un tipo de campo proporcionado por Django que se utiliza para almacenar y manejar imágenes. Al igual que otros campos de modelos en Django, ImageField representa una columna en la base de datos que guarda la información de la imagen.
    # Cuando se utiliza ImageField, Django maneja automáticamente la subida y el almacenamiento de la imagen en el sistema de archivos. Almacena la imagen en una ubicación específica y guarda la ruta de esa imagen en la base de datos.
    # Blank= true y null= true permite que sea opcional y pueda estar vacío en caso de que no se proporcione una imagen.#Buscar todas las configuraciones necesarias para que el programa pueda leer la imagen
    foto_perfil = models.ImageField(upload_to='img/fotos_perfil/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    