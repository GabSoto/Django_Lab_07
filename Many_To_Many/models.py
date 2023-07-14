from django.db import models

# Create your models here.

class Peliculas(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Actores(models.Model):
    name = models.CharField(max_length=20)
    pelis = models.ManyToManyField(Peliculas)

    def __str__(self):
        return self.name