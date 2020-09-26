"""
# Condicional IF

SI se_cumple_esta_condicion:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecuta otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras instrucciones
"""

# Ejemplo 1
print("################## EJEMPLO 1 ##################")

# color = "rojo"
color = input("¿Adivina cual es mi color favorito?: ")

if color == "rojo":
    print("Enhorabuena!!!")
    print("El color es ROJO")
else: 
    print("Color incorrecto")
    