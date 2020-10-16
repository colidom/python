"""
Proyecto Python y Mysql:
- Abrir asistente:
- Login o registro
- Si elegimos registro, creará un usuario en la ddbb
- Si elegimos login, identifica al usuario y nos preguntará
- Crear nota, mostrar notas, borrarlas
"""
from usuarios import acciones


print("""
Acciones disponibles:
    - registro
    - login
""")

# Instanciamos la clase (Creamos objeto)
hazEl = acciones.Acciones()

accion = input("¿Que quieres hacer?: ")

if accion == "registro":
    hazEl.registro()

elif accion == "login":
    hazEl.login()

