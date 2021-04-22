# Ejemplo: cuanta plata tiene

class Persona:
    """Una persona tiene amigos y billetes y puede prestar y recibir plata"""

    def __init__(self, nombre, billetes, caracter):
        self.nombre = nombre
        self.billetes = billetes
        self.amigos = []
        self.caracter = caracter

    def cuanto_tiene(self):
        return sum(self.billetes)

    def amigarse(self, amigo):
        self.amigos.append(amigo)

    def es_amigo(self, amigo):
        return amigo in self.amigos

    def recibir_billete(self, billete):
        self.billetes.append(billete)

    def sacar_billete(self, billete):
        self.billetes.remove(billete)

    def tiene_billete(self, billete):
        return billete in self.billetes

    def pedir_plata(self, billete, otraPersona):
        otraPersona.prestar_plata(billete, self)

    def prestar_plata(self, billete, otraPersona):
        self.caracter.prestar_plata(self, billete, otraPersona)

class Macanudo:
    """le presta a cualquiera mientras tenga billete"""

    def prestar_plata(self, persona, billete, otraPersona):
        if persona.tiene_billete(billete):
            persona.sacar_billete(billete)
            otraPersona.recibir_billete(billete)


class Amigazo(Macanudo):
    """le presta a los amigos si tiene billete"""

    def prestar_plata(self, persona, billete, otraPersona):
        if persona.es_amigo(otraPersona):
            super().prestar_plata(persona, billete, otraPersona)

        else:
            print("'No somos amigos'")


class Codito:
    """no le presta a nadie"""

    def prestar_plata(self, persona, billete, otraPersona):
        print("'No presto nada'")


# pepe = Persona("Pepe", [10, 20])
# print("Tiene: $", pepe.cuanto_tiene())

pepe = Persona("Pepe", [10, 20], Codito())
juan = Persona("Juan", [50, 100], Macanudo())
juan.amigarse(pepe)

print("Cuanto tiene Pepe?", pepe.cuanto_tiene())
print("Cuanto tiene Juan?", juan.cuanto_tiene())
print("Juan es amigo de Pepe?", juan.es_amigo(pepe))
print("Pepe es amigo de Juan?", pepe.es_amigo(juan))

pepe.pedir_plata(100, juan)
print("Cuanto tiene Pepe?", pepe.cuanto_tiene())
print("Cuanto tiene Juan?", juan.cuanto_tiene())
