# Ejemplo: cuanta plata tiene

class Persona:
    def __init__(self, nombre, billetes):
        self.nombre = nombre
        self.billetes = billetes

    def cuanto_tiene(self):
        return sum(self.billetes)


pepe = Persona("Pepe", [10, 20])

print("Tiene: $", pepe.cuanto_tiene())
