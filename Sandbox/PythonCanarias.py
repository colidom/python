# Método __str__
class Chicken:
    def __init__(self, weight):
        self.weight = weight
    def __str__(self):
        return f"A {self.weight}g chicken"
        
print(Chicken(1250))

# Protocolo de iteración

