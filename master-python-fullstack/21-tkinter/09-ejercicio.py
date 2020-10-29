"""
CALCULADORA:
- Dos campos de texto
- 4 botones para las operaciones
- Mostrar el resultado en una alerta
"""
from tkinter import *

ventana = Tk()
ventana.geometry("500x200")
ventana.title("Ejercicio completo con Tkinter | Carlos Oliva")
ventana.config(
    bd=25
)
numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

Label(ventana, text="Primer número: ").pack()
Entry(ventana, textvariable=numero1).pack()

Label(ventana, text="Segundo número: ").pack()
Entry(ventana, textvariable=numero2).pack()

# Separador
Label(ventana, text="").pack()

Button(ventana, text="Sumar").pack(side="left")
Button(ventana, text="Restar").pack(side="left")
Button(ventana, text="Multiplicar").pack(side="left")
Button(ventana, text="Dividir").pack(side="left")


ventana.mainloop()
