"""
CALCULADORA:
- Dos campos de texto
- 4 botones para las operaciones
- Mostrar el resultado en una alerta
"""
from tkinter import *

ventana = Tk()
ventana.geometry("500x250")
ventana.title("Ejercicio completo con Tkinter | Carlos Oliva")
ventana.config(
    bd=25
)
numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=300, height=250)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer número: ").pack()
Entry(marco, textvariable=numero1, justify=CENTER).pack()

Label(marco, text="Segundo número: ").pack()
Entry(marco, textvariable=numero2, justify=CENTER).pack()

# Separador
Label(marco, text="").pack()

Button(marco, text="Sumar").pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar").pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar").pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir").pack(side="left", fill=X, expand=YES)


ventana.mainloop()
