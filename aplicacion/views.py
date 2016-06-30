from aplicacion.models import Alumnos
from django.shortcuts import render_to_response

# Create your views here.

def mostrar(request):
 	return render_to_response('mostrar.html',{})
