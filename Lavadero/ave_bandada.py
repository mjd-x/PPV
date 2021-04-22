class Ave:
    def __init__(self):
        print("Se creó el ave.")

    def ensuciar(self, vehiculo):
        vehiculo.agregar_suciedad(1)

        print(f"El ave ensució el vehículo.")
        print(f"Suciedad del vehículo: {vehiculo.get_suciedad()}.")


class Paloma(Ave):
    """tipo de ave que ensucia 30% de su peso"""

    def __init__(self, peso):
        self.peso = peso
        print("Se creó la paloma.")

    def ensuciar(self, vehiculo):
        vehiculo.agregar_suciedad(0.3 * self.peso)
        self.peso -= self.peso * 0.3

        print(f"La paloma ensució el vehículo.")
        print(f"Suciedad del vehículo: {vehiculo.get_suciedad()}.")


class Gaviota(Ave):
    """tipo de ave que ensucia segun peces que comio"""

    def __init__(self, pescados):
        self.pescados = pescados
        print("Se creó la gaviota.")

    def ensuciar(self, vehiculo):
        vehiculo.agregar_suciedad(3 * self.pescados)
        print(f"La gaviota ensució el vehículo.")
        print(f"Suciedad del vehículo: {vehiculo.get_suciedad()}.")


class Bandada:
    """bandada compuesta de aves"""

    def __init__(self):
        self.aves = []
        print("Se creó la bandada.")

    def agregar_ave(self, ave):
        self.aves.append(ave)
        print("Se agregó el ave a la bandada.")

    def ensuciar(self, vehiculo):
        pass


class BandadaV(Bandada):
    """bandada en V, ensucian todas 1 vez"""

    def ensuciar(self, vehiculo):
        print(f"La bandada en V ensucia el vehículo.")
        for ave in self.aves:
            ave.ensuciar(vehiculo)

        print(f"Suciedad final del vehículo: {vehiculo.get_suciedad()}.")


class BandadaW(Bandada):
    """Bandada en W, ensucian todas 2 veces"""

    def ensuciar(self, vehiculo):
        print(f"La bandada en W ensucia el vehículo.")
        for ave in self.aves:
            ave.ensuciar(vehiculo)
            ave.ensuciar(vehiculo)

        print(f"Suciedad final del vehículo: {vehiculo.get_suciedad()}.")


class BandadaI(Bandada):
    """Bandada en I, ensucian la primera y la ultima"""

    def ensuciar(self, vehiculo):
        print(f"La bandada en I ensucia el vehículo.")
        self.aves[0].ensuciar(vehiculo)
        self.aves[(len(self.aves) - 1)].ensuciar(vehiculo)

        print(f"Suciedad final del vehículo: {vehiculo.get_suciedad()}.")
