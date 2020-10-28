from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
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

encabezado.pack(side=LEFT, anchor=NW, fill=X, expand=YES)

ventana.mainloop()
