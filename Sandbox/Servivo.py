class Servivo():
    def __init__(self, nombre, patas):
        self.nombre = nombre
        self.patas = patas
        self.comer = "comer"
        self.caminar = "caminar"


perro = Servivo("Dincky", "cuatro")
humano = Servivo("Carlos", 0)

print("El perro " + perro.nombre + " tiene " + perro.patas + " patas")
print("El humano "+ humano.nombre + " tiene un perro llamado " + perro.nombre + " que tiene " + perro.patas + " patas")
