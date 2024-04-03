from django.http import HttpResponse
from django.shortcuts import render

from STREAMING.forms import FormularioPelis
from STREAMING.models import Pelis


# Vista Inicial
def index (request):
    if request.method == "GET":
        formulario = FormularioPelis()  # Crea una instancia del formulario
        return render(request, 'STREAMING/index.html', {'formulario': formulario})
    elif request.method == "POST":
        return render(request, 'STREAMING/subir.html')

#Despliega Peliculas
def misPelis(request):
    peliculas = Pelis.objects.all()
    return render(request, 'STREAMING/catalogo.html',
                    #Se agrega diccionario para que pase la info de server a client
                    {"peliculas": peliculas, "titulo": "Mis peliculas"})