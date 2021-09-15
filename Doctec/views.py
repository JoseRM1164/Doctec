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


def Inicio(request): #primer vista

    return render(request, "inicio.html")

def Login(request):

    return render(request, "login.html")

def SignUp(request):

    return render(request, "signUp.html")

def Directorio(request):

    return render(request, "directorioDoc.html")

def InfoDoc(request):

    return render(request, "infoDoc.html")

#def adios(request): 
    
    #return HttpResponse("Adios Mundo")