from django.http import HttpResponse

def saludo(request): #primer vista

    return HttpResponse("Hola Mundo")

def adios(request): 
    
    return HttpResponse("Adios Mundo")