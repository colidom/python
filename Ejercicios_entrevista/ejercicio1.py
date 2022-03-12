"""
1. Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
Recuerda que python ya tiene un método max(), no podrás usarlo para resolver este ejercicio.
"""

def funcion_max(n1, n2):
    if n1 > n2:
        return n1
    elif n1 == n2:
        return "Ambos números son iguales"
    else:
        return n2


print(funcion_max(1, 1))
