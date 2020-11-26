from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones(métodos)
# MVT = Modelo Template Vista(vista = controlador) -> Acciones(métodos)

def index(request):
    
    nombre = 'Carlos Oliva'

    lenguajes = ['JavaScript', 'Python', 'PHP', 'C']
    
    return render(request, 'index.html', {
        'title': 'Inicio',
        'mi_variable': 'Soy un dato que está en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes
    })


def hola_mundo(request):
    return render(request, 'hola_mundo.html')


def pagina(request):
    return render(request, 'pagina.html')


def contacto(request, nombre="", apellidos=""):
    return render(request, 'contacto.html')
    
