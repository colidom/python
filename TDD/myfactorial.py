"""Enunciado
Supongamos que tenemos que implementar una función que 
calcule el factorial de un numero. Si seguimos al pie de 
la letra las indicaciones de TDD lo primero que tenemos 
que hacer es crear la función vacia simplemente para poder 
llamarla, implementar su test y ejecutarlo comprobando que 
falla.
Para ello debemos de crear un nuevo fichero al que llamaremos 
por ejemplo myfactorial.py en el que definiremos dicha función y 
crearemos un fichero llamado test_.py donde crearemos nuestra 
función test_myfactorial()
"""

def factorial(numero):
   fact = 1
   for i in range(1,numero+1):
      fact = fact * i
   return fact
