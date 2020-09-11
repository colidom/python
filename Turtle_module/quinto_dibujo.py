import turtle as t  # Importamos el módulo 

t.setup(500,500)

t.shape("turtle")   # Le damos la forma de una tortuga
t.color("green")    # Y un bonito color verde

# Un poquito de programación estructurada
def derecha():
    t.seth(0)
    t.forward(20)

def izquierda():
    t.seth(180)
    t.forward(20)

def arriba():
    t.seth(90)
    t.forward(20)

def abajo():
    t.seth(270)
    t.forward(20)

def salir():
    t.bye()

# Enlazamos cada función con una tecla
t.onkey(arriba, "w")
t.onkey(izquierda, "a")
t.onkey(derecha, "d")
t.onkey(abajo, "s")
t.onkey(salir, "e")

# Hacemos que la tortuga esté atenta a teclado
t.listen()

t.done()
t.by()
