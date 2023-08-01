from django.shortcuts import render, redirect
from django.template import Template, Context, loader
from django.http import HttpResponse
from datetime import datetime
from .models import Perro

# Create your views here.

def probando_template(self):
    
    # nombre1= "Chano"
    # apellido1 = "Vidili"
    # diccionario = {"nombre": nombre1, "apellido": apellido1, "hoy": datetime.now(), "notas": [1,2,3,4,5]}
    
    perro = Perro("Heraclito", "Labrador Dorado", 13)
    diccionario = {"nombre": perro.nombre, "raza": perro.raza, "edad": perro.edad}
    
    # plantilla = loader.get_template("template1.html")
    plantilla = loader.get_template("template2.html")
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)