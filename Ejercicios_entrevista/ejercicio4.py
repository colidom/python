"""
Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente 
todos los números de una lista. Por ejemplo sum([1, 2, 3, 4]) deberá devolver 10 y 
multip([1, 2, 3, 4]) deberá devolver 24.
"""

def sum(list):
    result = 0
    for n in list:
        result += n
    return result


def multip(a):
    total = 1
    for i in range(len(a)):
        total *= a[i]
    return total


list = [1, 2, 3, 4]

print(sum(list))
print(multip(list))