from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Producto(models.Model):
    codigo_producto = models.CharField(max_length=13,unique=True)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField(default=0, blank=True)
    stock = models.IntegerField(default=0, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion
    
class Categoria(models.Model):
    codigo_categoria = models.CharField(max_length=10,unique=True)
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_categoria
    
class Cliente(models.Model):
    rut = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True,blank=True,help_text="Formato: DD-MM-AAAA")
    email = models.EmailField(max_length=254,unique=True,help_text="Introduce una dirección de correo válida.")

    def __str__(self):
        return self.nombre



