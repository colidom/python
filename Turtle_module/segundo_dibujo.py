import turtle as t  # Importamos el módulo 

t.setup(500,500)

t.shape("turtle")   # Le damos la forma de una tortuga
t.color("green")    # Y un bonito color verde


print("Orígen", t.pos())
t.penup()
t.forward(150) 
t.left(90)  
t.pendown()
t.forward(150) 
print("Esquina superior derecha", t.pos())
t.left(90) 
t.forward(300)
print("Esquina superior izquierda", t.pos())
t.left(90) 
t.forward(300)
print("Esquina inferior izquierda", t.pos())
t.left(90) 
t.forward(300)
print("Esquina inferior derecha", t.pos())
t.left(90) 
t.forward(150)
print("Posición inicial", t.pos())

t.done()
t.by()
