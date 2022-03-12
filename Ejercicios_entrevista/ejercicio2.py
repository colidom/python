"""
Definir una función max_de_tres() que tome tres números como argumento y devuelva el mayor de ellos
"""

from turtle import rt


def max_de_tres(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    elif n3 > n1 and n3 > n2:
        return n2
    else: 
        if n1 == n2 or n1 == n3:
            return n1
        elif n2 == n1 or n2 == n3:
            return n2
        elif n3 == n1 or n3 == n2:
            return n3

print(max_de_tres(1, 2, 1))