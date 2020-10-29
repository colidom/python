import turtle as t  # Importamos el módulo 

t.setup(500,500)

t.shape("turtle")   # Le damos la forma de una tortuga
t.color("green")    # Y un bonito color verde

# Un poquito de programación estructurada

def rectangulo(px, py, ancho, alto):

    # Nos posicionamos en la esquina superior derecha
    # del rectángulo que vamos a dibujar sin dejar rastro
    # y miramos hacia la izquierda para empezar siempre igual

    t.penup()
    t.goto(px + ancho / 2, py + alto /2)
    t.setheading(180)
    t.pendown()


    t.forward(ancho)
    t.left(90)
    t.forward(alto)
    t.left(90)
    t.forward(ancho)
    t.left(90)
    t.forward(alto)

rectangulo(0, 0, 400, 300)
rectangulo(0, 0, 300, 200)
rectangulo(0, 0, 200, 100)
rectangulo(0, 0, 100, 50)
rectangulo(0, 0, 50, 26)


t.done()
t.by()
