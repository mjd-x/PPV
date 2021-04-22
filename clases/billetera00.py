# Ejemplo: cuanta plata tiene

class Persona:
    def __init__(self, nombre, billetera):
        self.nombre = nombre
        self.billetera = billetera

    def cuanto_tiene(self):
        return sum(self.billetera.get_billetes())


class Billetera:
    def __init__(self, billetes):
        self.billetes = billetes

    def get_billetes(self):
        return self.billetes

pepe = Persona("Pepe", Billetera([10, 20]))

print("Tiene: $", pepe.cuanto_tiene())
