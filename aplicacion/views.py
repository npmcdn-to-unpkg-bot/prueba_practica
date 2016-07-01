from aplicacion.models import Alumnos
from django.shortcuts import render_to_response

# Create your views here.

def mostrar(request):
 	return render_to_response('mostrar.html',{})

def ej1(request):
 	return render_to_response('ej1.html',{})

def ej2(request):
 	return render_to_response('ej2.html',{})

def ej3(request):
 	return render_to_response('ej3.html',{})	

def ej4(request):
 	return render_to_response('ej4.html',{})	 	

def barra(request):
 	return render_to_response('barra6.html',{})	