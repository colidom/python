import pyautogui as pygui
import time 

# Definimos el contador para realizar un número determinado de procesos
def accionRaton():
        # Movemos el cursor a las coordenadas indicadas y realizamos una acción 
        # Izquierda y clic derecho
        pygui.moveTo(300, 100, duration=0.1)
        pygui.rightClick()

        # Movemos el cursor hacia abajo y hacemos clic izquierdo
        pygui.moveTo(360, 160)
        pygui.leftClick()

        # Derecha y clic derecho
        pygui.moveTo(2150, 100, duration=0.1)
        pygui.rightClick()

        # Movemos el cursor hacia abajo y hacemos clic izquierdo
        pygui.moveTo(2200, 160)
        pygui.leftClick()
        

  
# Indicamos el número de acciones que deseamos realizar y durante que tiempo en segundos
numAcciones = int(input("Inserte el número de acciones a realizar: ")) 
intervaloTiempo = int(input("Cada cuanto tiempo en segundos desea lanzar la función?: "))

acciones = 1

# Bucle para realizar el número de acciones indicadas por el usuario
while numAcciones:
    # Esperamos el tiempo indicado por el usuario, en segundos
    time.sleep(intervaloTiempo)
    accionRaton()
    print(f"\nNúmero de acciones realizadas: {acciones}")
    numAcciones -= 1
    acciones += 1 
    print(f"Número de acciones restantes:  {numAcciones}")
