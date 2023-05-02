# Estos son los datos que vamos a soliciar para cada contacto
campos = ("nombre", "apellidos", "email", "teléfono")

# Esta lista contendrá todos los contactos
contactos: list = []

# Inicializamos la variable seguir
seguir = "s"

# Mientras el valor a seruir sea 's' o 'S' introducimos contactos
while seguir in ("s", "S"):
    # Este diccionario almacena los valores de un contacto
    contacto: dict = {}

    # Con este bucle preguntamos campo a campo
    for campo in campos:
        valor = input(campo + ": ")

        # Si el usuario introduce algo, se almacena
        if len(valor) > 0:
            contacto[campo] = valor

            # Añadimos el contacto a la lista
            contactos.append(contacto)

            # Preguntamos si seguimos añadiendo contactos
            seguir = input("¿Introducir otro contacto? s/n: ")

    # Mostramos todos los contactos
    for contacto in contactos:
        for k, v in contacto.items():
            print(k + ": " + v)

        # Mostramos esto para finalizar la lectura
        print("---------")
