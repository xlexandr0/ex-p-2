from django.db import models

class Compania(models.Model):
    nombre = models.CharField(max_length=200)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Videojuego(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    anio_lanzamiento = models.PositiveSmallIntegerField()
    compania = models.ForeignKey(Compania, related_name='videojuegos', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} ({self.anio_lanzamiento})"
