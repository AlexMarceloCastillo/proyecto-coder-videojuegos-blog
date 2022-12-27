from django.db import models
# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    foto_url = models.CharField(max_length=255)

class Categoria(models.Model):
    nombre = models.CharField(max_length=40)

class Post(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40)
    contenido = models.TextField()
    fecha_creacion = models.DateField()
    imagen_url = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Desarrollador(models.Model):
    nombre = models.CharField(max_length=100)
    fundacion = models.DateField()
    web_url = models.CharField(max_length=255)

class Genero(models.Model):
    nombre = models.CharField(max_length=40)
    fecha_creacion = models.DateField()

class Plataforma(models.Model):
    nombre = models.CharField(max_length=40)
    fecha_lanzamiento = models.DateField()

class Videojuego(models.Model):
    nombre = models.CharField(max_length=255)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    desarrollador = models.ForeignKey(Desarrollador, on_delete=models.CASCADE)
    fecha_lanzamiento = models.DateField()
    plataformas = models.ManyToManyField(Plataforma)
