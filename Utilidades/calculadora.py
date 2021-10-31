import math
class calculadora():
    
    def suma(n1, n2):
        return n1 + n2
    
    def resta(n1, n2):
        return n1 - n2

    def dividir(n1, n2):
        return n1 / n2

n1 = float(input("Primer numero: "))
n2 = float(input("Segundo numero: "))

suma = calculadora.suma(n1, n2)
resta = calculadora.resta(n1, n2)
division = calculadora.dividir(n1, n2)

print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La división es: {division}")
