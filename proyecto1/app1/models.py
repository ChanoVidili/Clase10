from django.db import models

# Create your models here.

class Perro(models.Model):
    nombre = models.CharField(max_length=30)
    raza = models.CharField(max_length=30)
    edad = models.IntegerField()