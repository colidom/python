diccionario = "TRWAGMYFPDXBNJZSQVHLCKE"
cadena = "22312313212301234704"

letra = int(cadena) % 23
codigoControl = diccionario[letra]
print("El código de envío es: " + (f"{cadena}{codigoControl}"))
