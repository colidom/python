import turtle as t  # Importamos el módulo 

t.setup(500,500)

t.shape("turtle")   # Le damos la forma de una tortuga
t.color("green")    # Y un bonito color verde

# Un poquito de programación estructurada

def poligono_regular(px, py, radio, lados):
    t.penup()
    t.goto(px, py - radio)
    t.pendown()
    t.circle(radio)

    angulo = 360 / lados
    print(angulo)

    vertices = []

    for i in range(lados):
        t.penup()                   # Nos posicionamos en el centro
        t.goto(px, py)
        t.pendown()

        t.seth(angulo*i+1)          # Trazamos radios hacia fuera
        t.forward(radio)
        vertices.append(t.pos())    # Los vamos añadiendo a la lista

    # Nos posicionamos en la coordenada del primer vértice
    t.penup()
    t.goto(vertices[-1])
    t.pendown()

    # Y hacemos que la tortuga se mueva a cada uno de ellos
    for v in vertices:
        t.goto(v)

# Hacemos que la tortuga se mueva muy rápido y dibujamos
# los polígonos regulares de 3 a 20 costados
t.speed(200)
for n in range(3, 21):
    poligono_regular(0, 0, n*10, n)


t.done()
t.by()
