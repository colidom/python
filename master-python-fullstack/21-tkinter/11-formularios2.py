from tkinter import *


ventana = Tk()
ventana.geometry("800x300")

encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Consolas", 20)
)
encabezado.pack(anchor=N, fill=X, expand=YES, side=TOP)

# Botones check


# Radio buttons


# Option Menu
ventana.mainloop()
