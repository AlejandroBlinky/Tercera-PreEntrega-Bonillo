from django.shortcuts import render
from django.http import HttpResponse
from AppPlayground.forms import * 
from AppPlayground.models import *


# Create your views here.

def inicio(request):
    return render(request,"AppPlayground/inicio.html")

def cursos(request):
    return render(request,"AppPlayground/cursos.html")

def profesores(request):
    return render(request,"AppPlayground/profesores.html")

def estudiantes(request):
    return render(request,"AppPlayground/estudiantes.html")

    
    
def setEstudiantes(request):
    if request.method == 'POST':
        miFormulario = formSetEstudiante(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():  # Corrección aquí
            data = miFormulario.cleaned_data
            estudiante = Estudiante(nombre=data["nombre"],apellido=data["apellido"], email=data["email"])    
            estudiante.save()
            return render(request, "AppPlayground/getEstudiantes.html")    
    else:
        miFormulario = formSetEstudiante()
    return render(request, "AppPlayground/setEstudiantes.html", {"miFormulario":miFormulario})
def getEstudiantes(request):
    return render(request, "AppPlayground/getEstudiantes.html")


def buscarEstudiantes(request):
    nombre = request.GET.get("nombre")
    if nombre:
        estudiantes = Estudiante.objects.filter(nombre=nombre)
        return render(request, "AppPlayground/getEstudiantes.html", {"estudiantes": estudiantes})
    else:
        return render(request, "AppPlayground/getEstudiantes.html")


def setCursos(request):
    if request.method == 'POST':
        miFormulario = formSetCurso(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():  # Corrección aquí
            data = miFormulario.cleaned_data
            curso = Curso(nombre=data["nombre"],camada=data["camada"],)    
            curso.save()
            return render(request, "AppPlayground/getCursos.html")    
    else:
        miFormulario = formSetCurso()
    return render(request, "AppPlayground/setCursos.html", {"miFormulario":miFormulario})

def getCursos(request):
    return render(request, "AppPlayground/getCursos.html")


def buscarCursos(request):
    nombre = request.GET.get("nombre")
    if nombre:
        cursos = Curso.objects.filter(nombre=nombre)
        return render(request, "AppPlayground/getCursos.html", {"cursos": cursos})
    else:
        return render(request, "AppPlayground/getCursos.html")
    
    
    
def setProfesores(request):
    if request.method == 'POST':
        miFormulario = formSetProfesor(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():  # Corrección aquí
            data = miFormulario.cleaned_data
            profesor = Profesor(nombre=data["nombre"],apellido=data["apellido"],email=data["email"],profesion=data["profesion"])    
            profesor.save()
            return render(request, "AppPlayground/getProfesores.html")    
    else:
        miFormulario = formSetProfesor()
    return render(request, "AppPlayground/setProfesores.html", {"miFormulario":miFormulario})

def getProfesores(request):
    return render(request, "AppPlayground/getProfesores.html")


def buscarProfesores(request):
    nombre = request.GET.get("nombre")
    if nombre:
        profesores = Profesor.objects.filter(nombre=nombre)
        return render(request, "AppPlayground/getProfesores.html", {"profesores": profesores})
    else:
        return render(request, "AppPlayground/getProfesores.html")






    