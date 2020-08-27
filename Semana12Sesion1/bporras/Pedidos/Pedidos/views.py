from django.http import HttpResponse
import datetime
from django.shortcuts import render
def saludo(request):
    nombre = "Juan"
    apellido = "Diaz"
    return render(request,"miplantilla.html",{"nombre_persona":nombre, "apellido_persona":apellido, "temas": ["futbol","deporte","domingo"]})

def despedida(request):

    return HttpResponse("Hasta luego alumnos de django")

def fecha(request):
    fecha_actual=datetime.datetime.now()
    documento = f"""<html>
    <body>
    <h2>
    Fecha y hora actuales: {fecha_actual}
    </h2>
    </body>
    </html>"""  
    return HttpResponse(documento)
def calculaEdad(request, age, year):
    periodo = year - 2020
    edad_futura = age + periodo
    documento = f"""<html>
    <body>
    <h2>
    En el año {year} tendras {edad_futura} años
    </h2>
    </body>
    </html>"""  
    return HttpResponse(documento)

def cursoC(request):
    fecha_actual=datetime.datetime.now()
    return render(request,"CursoC.html",{"dameFecha":fecha_actual})
def cursoCSS(request):
    fecha_actual=datetime.datetime.now()
    return render(request,"CursoCSS.html",{"dameFecha":fecha_actual})