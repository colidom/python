import random

users = ["Carlos","Pepe","Luis","María","Alberto", "Marta"]

try:
  while True:
    print("")
    print("___Lista de opciones___")
    print("1. Roll")
    print("2. Exit")
    option = input("Por favor elija una opción: ")
    print(option)
    if option == "1":
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