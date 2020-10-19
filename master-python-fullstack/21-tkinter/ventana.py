# Tkinter
# Módulo para crear interfaces gráficas de usuario

from tkinter import *

# Crear la ventana raiz
ventana = Tk()

# Título de la ventana
ventana.title("Interfaz gráfica con Python")
# Icono de la ventana
ventana.iconbitmap("./21-tkinter/imagenes/logo.ico")

# Cambio en el tamaño de la ventana
ventana.geometry("750x450")

# Bloquear el tamaño de la ventana
ventana.resizable(0, 0)


# Arrancar y mostrar la ventana hasta que se cierre
ventana.mainloop()
