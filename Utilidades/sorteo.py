import random

participants_list = []

try:
  while True:
    print("")
    print("___Lista de opciones___")
    print("1. Añadir participante")
    print("2. Roll")
    print("3. Salir")
    option = input("Por favor elija una opción: ")
    print(option)

    if option == "1":
      competitor = input("Introduzca el nombre del competitor: ")
      participants_list.append(competitor)
      print("")
      print(f"Se ha añadido el competitor [{competitor}] a la lista")
      print(f"___Listado de participantes___")
      print(participants_list)
    elif option == "2":
      random.shuffle(participants_list)
      winner = participants_list.pop(1)
      print(f"Opcion elegida: {option}")
      print(f"Lista de usuarios: {participants_list}")
      print(f"")
      print(f"Usuario ganador: {winner}")
      print(f"******************************")
    else: 
      print("Hasta luego.")
      break
except:
  print("Todos los usuarios han recibido su premio.")
  