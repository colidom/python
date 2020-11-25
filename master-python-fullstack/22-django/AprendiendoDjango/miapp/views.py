from django.shortcuts import render, HttpResponse

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones(métodos)
# MVT = Modelo Template Vista(vista = controlador) -> Acciones(métodos)

layout = """
<h1>Sitio web con Django | Carlos Oliva</h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola Mundo</a>
    </li>
    <li>
        <a href="/pagina-pruebas">Página pruebas</a>
    </li>
</ul>
<hr/>
"""
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
    return HttpResponse(layout + html)

def hola_mundo(request):
    return HttpResponse(layout + """
        <h1>Hola Mundo con Django!!</h1>
        <h3>Soy Carlos Oliva</h3>
    """)

def pagina(request):
    return HttpResponse(layout + """
        <h1>Página de mi web</h1>
        <p>Creado por Carlos Oliva</p>
    """)
