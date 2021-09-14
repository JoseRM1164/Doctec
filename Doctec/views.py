from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

#Proyecto

class Persona(object):
    
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido


def saludo(request): #primer vista

    p1=Persona(" Profe Juan", "Montoya")

    temas_curso=["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]

    ahora=datetime.datetime.now()
 
    #doc_externo=open("C:/Users/Windows 10/Documents/Ultimo Semestre/Lab. Web/Proyecto/Doctec/Doctec/Template/inicio.html")
    #temp= Template(doc_externo.read())
    #doc_externo.close()
    #doc_externo=get_template('inicio.html')
    #ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "hora_actual":ahora, "temas":temas_curso})
    #documento=doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "hora_actual":ahora, "temas":temas_curso})

    return render(request, "inicio.html", {"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "hora_actual":ahora, 
    "temas":temas_curso})

def adios(request): 
    
    return HttpResponse("Adios Mundo")

def dameFecha(request):

    fecha_actual=datetime.datetime.now()
    return HttpResponse("Fecha y hora actuales %s " % fecha_actual)

def prueba(request):

    ahora=datetime.datetime.now()
    return render(request, "Prueba.html", {"hora_actual":ahora})

def prueba2(request):

    return render(request, "Prueba2.html")
