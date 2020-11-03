"""
Crear un programa que tenga:
- Ventana
- Tamaño fijo
- No redimensionable
- Un menu (Inicio, Añadir, Información, Salir)
- Diferentes pantallas
- Formulario de añadir productos
- Guardar datos temporalmente
- Mos trar datos listados en la pantalla home
"""
from tkinter import *

# Definir ventana
ventana = Tk()
ventana.geometry("500x500")
ventana.title("Proyecto Tkinter - Master en Python")
ventana.resizable(0, 0)

# Pantallas
def home():
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    home_label.grid(row=0, column=0)

    # Ocultar otras pantallas
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    
def add():
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    add_label.grid(row=0, column=0)

    # Ocultar otras pantallas
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)
    
    # Ocultar otras pantallas
    home_label.grid_remove()
    add_label.grid_remove()
    data_label.grid_remove()

# Definir campos de pantalla (INICIO)
home_label = Label(ventana, text="Inicio")

# Definir campos de pantalla (ADD)
add_label = Label(ventana, text="Añadir producto")

# Definir campos de pantalla (INFORMACION)
info_label = Label(ventana, text="Información")
data_label = Label(ventana, text="Creado por Carlos Oliva - 2020")

# Cargar pantalla inicio
home()
add()
info()

# Menú superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=(ventana.quit))

# Cargar menú
ventana.config(menu=menu_superior)

# Cargar ventana
ventana.mainloop()
