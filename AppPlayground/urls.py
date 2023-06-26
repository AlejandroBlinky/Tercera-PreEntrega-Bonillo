from django.urls import path
from .views import *

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('cursos/', cursos, name="Cursos"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('profesores/', profesores, name="Profesores"),
    path('setEstudiantes/', setEstudiantes, name="setEstudiantes"),
    path('buscarEstudiantes/', buscarEstudiantes, name="buscarEstudiantes"),
    path('buscarCursos/', buscarCursos, name="buscarCursos"),
    path('setCursos/', setCursos, name="setCursos"),
    path('setProfesores/', setProfesores, name="setProfesores"),
    path('buscarProfesores/', buscarProfesores, name="buscarProfesores"),
    
    
    
    
    # Otras rutas de URLs aquí...
]

