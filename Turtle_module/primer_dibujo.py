import turtle as t  # Importamos el módulo 

t.setup(500,500)

t.shape("turtle")   # Le damos la forma de una tortuga
t.color("green")    # Y un bonito color verde

print("Orígen", t.pos())
t.forward(200) 
t.left(90)     
print("Esquina superior derecha", t.pos())
t.forward(200)
t.left(90)  
t.forward(400)
print("Esquina superior izquierda", t.pos())
t.left(90)  
t.forward(400)
t.left(90)  
print("Esquina inferior izquierda", t.pos())
t.forward(400)
print("Esquina inferior derecha", t.pos())


t.done()
t.by()
