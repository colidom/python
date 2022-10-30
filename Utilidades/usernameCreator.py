"""
Crea nombre de usuario a partir de Nombre y dos Apellidos
"""

name = input("Introduzca su nombre: ")
surname1 = input("Introduzca su primer apellido: ")
surname2 = input("Introduzca su segundo apellido: ")

userPartOne = name[0:1].lower()
userPartTwo = surname1[0:3].lower()
userPartTree = surname2[0:3].lower()

print(f"Su nombre de usuario es: {userPartOne}{userPartTwo}{userPartTree}")
