class Coche:

    marca = "Audi"
    modelo = "A5 Sline"
    combustible = "Gasolina"
    color = "Azul"
    estado = "Apagado"
    velocidad = 0
    marchaActual = 0
    velocidadMax = 290

    # Setters
    def setAcelerar(self):
        self.velocidad += 1

    def setFrenar(self):
        self.velocidad -= 1

    def setSubirMarcha(self):
        self.marchaActual += 1

    def setBajarMarcha(self):
        self.marchaActual -= 1

    def setEstado(self, estado):
        self.estado = estado
    
    def setColor(self, color):
        self.color = color

    # Getters
    def getColor(self):
        return self.color
        
    def getEstado(self):
        return self.estado
    
    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo
    
    def getCombustible(self):
        return self.combustible
    
    def getVelocidad(self):
        return self.velocidad
    
    def getMarchaActual(self):
        return self.marchaActual

    def getVelocidadMax(self):
        return self.velocidadMax

# Instanciamos la clase Coche
coche = Coche()

cambiarColor = input(f"El color por defecto del coche es: {coche.getColor()}. ¿Desea cambiarlo? 'SI/NO': ")

if cambiarColor == "si" or cambiarColor == "SI":
    color = input("¿De que color quieres pintarlo?: ")
    coche.setColor(color)
    print(f"El nuevo color de su coche es: {coche.getColor()}")
else:
    print(f"Muy bien, ha elegido el color por defecto del coche: {coche.getColor()}")

print("\n****** Coche aparcado ******")
print(f"Marca: {coche.getMarca()}")
print(f"Modelo: {coche.getModelo()}")
print(f"Color: {coche.getColor()}")
print(f"Combustible: {coche.getCombustible()}")
print(f"Velocidad máxima: {coche.getVelocidadMax()} kms/h")
print(f"Estado: {coche.getEstado()}")

print("\n****** Nos subimos al coche ******")
print("¡Nos ponemos el cinturón de seguridad!")
print("Metemos la llave y arrancamos")
coche.setEstado("Arrancado")
print(f"El coche está en estado '{coche.getEstado()}', puede conducirlo")

print("\n****** Nos disponemos a salir ******")
coche.setSubirMarcha()
print(f"Metemos: {coche.getMarchaActual()} y aceleramos")
coche.setAcelerar()
print(f"{coche.getVelocidad()} kms/h")
coche.setAcelerar()
print(f"{coche.getVelocidad()} kms/h")
coche.setAcelerar()
print(f"{coche.getVelocidad()} kms/h")
coche.setSubirMarcha()
print(f"Metemos {coche.getMarchaActual()} y seguimos acelerando")
coche.setAcelerar()
print(f"{coche.getVelocidad()} kms/h")
coche.setAcelerar()
print(f"{coche.getVelocidad()} kms/h")
coche.setAcelerar()
print(f"{coche.getVelocidad()} kms/h")
print(f"Metemos segunda: {coche.getMarchaActual()}")

print(f"Velocidad actual: {coche.getVelocidad()} kms/h")

