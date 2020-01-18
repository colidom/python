def sumar(n1, n2):
    resultado = (n1 + n2)
    text = "La suma de {} y {} es: {}".format(n1, n2, resultado) 
    text2 = f"La suma de {n1} y {n2} es: {resultado}"
    print(text)
    print(text2)


n1 = int(input("N1: "))
n2 = int(input("N2: "))

sumar(n1, n2)
