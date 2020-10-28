from tkinter import *

ventana = Tk()
ventana.geometry("500x400")
ventana.title("Formularios en Tkinter | Carlos Oliva")

# Texto encabezado
encabezado = Label(ventana, text="Formularios con Tkinter | Carlos Oliva")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 18),
    padx=10,
    pady=10
)

encabezado.grid(row=0, column=0, columnspan=3, sticky=NW)

# Label para el campo(nombre)
label = Label(ventana, text="Nombre: ")
label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Campo de texto
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state="normal")

# Label para el campo(apellidos)
label = Label(ventana, text="Apellidos: ")
label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Campo de texto
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state="normal")

ventana.mainloop()
