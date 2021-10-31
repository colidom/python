diccionario = "TRWAGMYFPDXBNJZSQVHLCKE"
dni = int(input("Por favor introduzca su nº DNI sin la letra: "))

letra = dni % 23
digitoControl = diccionario[letra]
print(f"Su número fiscal (NIF) es: {dni}{digitoControl}")
