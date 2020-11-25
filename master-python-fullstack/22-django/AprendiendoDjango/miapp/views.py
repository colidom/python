from django.shortcuts import render, HttpResponse

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones(métodos)
# MVT = Modelo Template Vista(vista = controlador) -> Acciones(métodos)

def index(request):

    html = """
        <h1>Inicio</h1>
        <p>Años hasta el 2050:</p>
    """
    year = 2020

    while year <= 2050:

        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year +=1

    html += "</ul>"
    return HttpResponse(html)

def hola_mundo(request):
    return HttpResponse("""
        <h1>Hola Mundo con Django!!</h1>
        <h3>Soy Carlos Oliva</h3>
    """)

def pagina(request):
    return HttpResponse("""
        <h1>Página de mi web</h1>
        <p>Creado por Carlos Oliva</p>
    """)
