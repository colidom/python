class calculadora:
    
    def suma(num1, num2):
        return num1 + num2
    
    def resta(num1 , num2):
        return num1 - num2

resultadoSuma = calculadora.suma(10, 10)
resultadoResta = calculadora.suma(122, 10)

print(f"El resultado de la suma es: {resultadoSuma}")
print(f"El resultado de la resta es: {resultadoResta}")
