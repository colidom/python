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
encabezado.grid(row=0, column=0, columnspan=5, sticky=W)

# Botones check
web = IntVar()
movil = IntVar()

def mostrarProfesion():
    texto = ""

    if web.get():
        texto += "Desarrollo web"

    if movil.get():
        if web.get():
            texto += " y Desarrollo Movil"
        else:
            texto += "Desarrollo movil"

    mostrar.config(
        text=texto,
        bg="green",
        fg="white"
    )


Label(ventana, text="¿A que te dedicas?").grid(row=1, column=0)
Checkbutton(
    ventana, 
    text="Desarrollo Web",
    variable = web,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=2, column=0)
Checkbutton(
    ventana, 
    text="Desarrollo movil",
    variable=movil,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=3, column=0)

mostrar = Label(ventana)
mostrar.grid(row=4, column=0)

# Radio buttons


# Option Menu


ventana.mainloop()
