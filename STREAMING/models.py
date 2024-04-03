from django.db import models


# Modelo = Tabla
# Tabla de Peliculas
class Pelis(models.Model):
    titulo = models.CharField(max_length=500)
    sinopsis = models.CharField(max_length=500)
    director = models.CharField(max_length=100)
    fechaLanzamiento = models.DateField()

# Tabla de Generos
class Generos(models.Model):
    pelicula = models.ForeignKey(Pelis, on_delete=models.CASCADE)
    genero = models.CharField(max_length=50)