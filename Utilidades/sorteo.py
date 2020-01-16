import random

users = []

try:
  while True:
    print("")
    print("___Lista de opciones___")
    print("1. Añadir participante")
    print("2. Roll")
    print("3. Exit")
    option = input("Por favor elija una opción: ")
    print(option)

    if  option == "1":
      nombre = input("Introduzca el nombre del participante: ")
      users.append(nombre)
      print(f"Hay {users} usuarios")
    elif option == "2":
        random.shuffle(users)
        agraciado = users.pop(1)
        print(f"Opcion elegida: {option}")
        print(f"Lista de usuarios: {users}")
        print(f"Usuario agraciado: {agraciado}")
    else: 
        print("Hasta luego")
        break
except:
  print("Todos los usuarios han recibido su premio.")