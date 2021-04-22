class Persona:
    """Cualquier persona puede contraer enfermedades."""

    def __init__(self, temperatura, celulas):
        self.temperatura = float(temperatura)
        self.celulas = int(celulas)
        self.enfermedades = []

        print("Persona creada.")

    def get_temperatura(self):
        return self.temperatura

    def set_temperatura(self, temp):
        self.temperatura = temp

    def get_celulas(self):
        return self.celulas

    def set_celulas(self, cels):
        self.celulas = cels

    def contraer(self, enfermedad):
        self.enfermedades.append(enfermedad)

        print("La persona contrajo la enfermedad.")

    def ver_estado(self):
        print(f"Temperatura: {self.temperatura}")
        print(f"Células: {self.celulas}")
        print(f"Tiene {len(self.enfermedades)} enfermedad/es.")

    def dia_siguiente(self):
        """En el momento que se contrae una enfermedad, esta no le causa ningún efecto,
           pero cada día que vive una persona con su enfermedad se producen sus consecuencias."""

        for enfermedad in self.enfermedades:
            enfermedad.efecto(self)

        print("Pasó un día.")

    def curarse(self):
        """Una enfermedad se considera curada si no amenaza a ninguna célula."""

        for enfermedad in self.enfermedades:
            if enfermedad.get_celulasAfectadas() <= 0:
                self.enfermedades.remove(enfermedad)

                print("La persona se curó de una enfermedad.")

    def tomar_medicacion(self, cantidad):
        """en el caso en que la persona reciba un medicamento,
           las enfermedades que tiene en el cuerpo se atenúan
           (cada una se atenúa en la cantidad de medicamento recibida, multiplicada por 15)."""

        print(f"La persona tomó {cantidad} ml de medicación.")

        for enfermedad in self.enfermedades:
            enfermedad.set_celulasAfectadas(enfermedad.get_celulasAfectadas() - (cantidad * 15))
            if enfermedad.get_celulasAfectadas() <= 0:
                self.curarse()

class Enfermedad:
    """De alguna enfermedad en particular, se conoce la cantidad de células que
       amenaza de la persona enferma"""

    def __init__(self, celulasAfectadas):
        self.celulasAfectadas = celulasAfectadas

        print("Enfermedad creada.")

    def set_celulasAfectadas(self, celulas):
        self.celulasAfectadas = celulas

    def get_celulasAfectadas(self):
        return self.celulasAfectadas

    def atenuar(self, cantidad):
        """Cuando una enfermedad se atenúa, baja la cantidad de células amenazadas por ella."""

        self.celulasAfectadas -= cantidad

        print("Se atenuó la enfermedad.")

    def efecto(self, persona):
        pass


class EnfermedadInfecciosa(Enfermedad):
    def efecto(self, persona):
        """Las enfermedades infecciosas (como la malaria) aumentan la temperatura de la
           persona infectada en tantos grados como la milésima parte de las células amenazadas"""

        persona.set_temperatura(persona.get_temperatura() - self.celulasAfectadas / 1000)

    def reproducirse(self):
        """las enfermedades infecciosas pueden reproducirse a sí mismas,
           duplicando la cantidad de células amenazadas."""

        self.celulasAfectadas *= 2


class EnfermedadAutoinmune(Enfermedad):
    def efecto(self, persona):
        """Las enfermedades autoinmunes (como el lupus) destruyen la cantidad de células amenazadas"""

        persona.set_celulas(persona.get_celulas() - self.celulasAfectadas)

