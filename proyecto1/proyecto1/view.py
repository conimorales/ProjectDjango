from multiprocessing import context
from pipes import Template
from django.http import HttpResponse
from django.template import Context, Template

from Appcoder.models import Falimiares
from django.shortcuts import render

def probandoTemplate(request):
    mihtml = open(r"C:\Users\conaa\OneDrive\Desktop\coderhouse\python\proyecto_1\ProyectoDjango\proyecto1\proyecto1\templates\template1.html")
    plantilla = Template(mihtml.read())
    mihtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

''' def familia(request, nombre, edad, fecha_nacimiento):
    familia = Falimiares(nombre= nombre, edad = edad, fecha_nacimiento = fecha_nacimiento)
    
    return HttpResponse(f"""
                        <p> Nombre: {familia.nombre}</p>
                        <p> Edad: {familia.edad}</p>
                        <p> Cumpleaños: {familia.fecha_nacimiento}</p>
                        
                        
                        """) '''

def familia(request):
    familia = Falimiares.objects.all()
    return render(request, "lista_familiares.html", {"lista_familiares": familia})