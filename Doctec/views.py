from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

#Proyecto

#class Persona(object):
    
   # def __init__(self, nombre, apellido):
      #  self.nombre=nombre
        #self.apellido=apellido


def inicio(request): #primer vista

    return render(request, "inicio.html")

def login(request):

    return render(request, "login.html")

def signUp(request):

    return render(request, "signUp.html")

def directorio(request):

    return render(request, "directorioDoc.html")

def infoDoc(request):

    return render(request, "infoDoc.html")

def contacto(request):

    return render(request, "contacto.html")

def servicios(request):

    return render(request, "servicios.html")

#def adios(request): 
    
    #return HttpResponse("Adios Mundo")