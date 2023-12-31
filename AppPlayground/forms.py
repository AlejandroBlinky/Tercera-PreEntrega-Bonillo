from django import forms 

class formSetEstudiante(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    
    
class formSetProfesor(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)
    
class formSetCurso(forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()