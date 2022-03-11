# -*- coding: utf-8 -*-

class Humano: #Creamos la clase Humano
    def __init__(self, edad, nombre, ocupacion): #Definimos el parametro edad , nombre y ocupacion
        self.edad = edad # Definimos que el atributo edad, sera la edad asignada
        self.nombre = nombre # Definimos que el atributo nombre, sera el nombre asig
        self.ocupacion = ocupacion #DEFINIMOS EL ATRIBUTO DE INSTANCIA OCUPACION
        
        #Creación de un nuevo método
    def presentar(self):
        print(f"Hola soy {self.nombre}, mi edad es {self.edad} y mi ocupación es {self.ocupacion}") #Mensaje
        

    #Creamos un nuevo método para cambiar la ocupación:
    #En caso que esta persona sea contratada
        
    def contratar(self, puesto): #añadimos un nuevo parámetro en el método
        self.puesto = puesto
        print (f"{self.nombre} ha sido contratado como {self.puesto}")
        self.ocupacion = puesto #Ahora cambiamos el atributo ocupación

Persona1 = Humano(31, "Pedro", "Desocupado") #Instancia

#Llamamos al método
Persona1.presentar() 
Persona1.contratar("Obrero")
Persona1.presentar() #Lo volvemos a presentar luego de su contratación
