class Vehiculo:
    def __init__(self, suciedad, ultLavado):
        self.suciedad = float(suciedad)
        self.ultLavado = int(ultLavado)

        print(f"Se creó el vehículo.")

    def limpiar(self):
        self.suciedad = 0
        self.ultLavado = 0

    def agregar_suciedad(self, suciedad):
        self.suciedad += suciedad

    def get_suciedad(self):
        return self.suciedad

    def suciedad_simple(self):
        """se suma 0,1 a suciedad por cada dia desde el ultimo lavado"""
        self.suciedad += 0.1 * self.ultLavado  # ???


class Ciudad:
    def __init__(self):
        self.vehiculos = []
        self.lavaderos = []

        print(f"Se creó la ciudad.")

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

        print(f"Se agregó el vehículo a la ciudad.")

    def agregar_lavadero(self, lavadero):
        self.lavaderos.append(lavadero)

        print(f"Se agregó el lavadero a la ciudad.")

    def lluvia_ceniza(self, mm):
        """Cae lluvia de ceniza volcanica en la ciudad, ensuciando a todos los autos ahi"""
        for vehiculo in self.vehiculos:
            vehiculo.agregar_suciedad(mm)

        print(f"Cayó una lluvia de ceniza volcánica de {mm}mm sobre la ciudad,")
        print(f"ensuciando a todos los autos que estaban ahí.")

    def mas_barato(self):
        """busca cual es el lavadero mas barato de la ciudad"""
       # menor = self.lavaderos[0].costo

       # for lavadero in self.lavaderos:
       #     if lavadero.costo < menor:
       #         menor = lavadero.costo

        menor = min(self.lavaderos, key=lambda lavadero: lavadero.costo)

        print(f"El lavadero más barato cuesta ${menor}.")


class Lavadero:
    def calcular_precio(self):
        pass

    def calcular_tiempo(self):
        pass

    def lavar(self, vehiculo):
        print(f"Se lavó el vehículo.")
        self.calcular_precio(vehiculo)
        self.calcular_tiempo(vehiculo)
        vehiculo.limpiar()


class LavAutomatico(Lavadero):
    """Lavadero automatico, cobra siempre lo mismo y tarda siempre lo mismo"""

    def __init__(self, costo, tiempo):
        self.costo = costo
        self.tiempo = tiempo

        print(f"Se creó el lavadero.")

    def calcular_precio(self):
        print(f"Salió ${self.costo}.")

    def calcular_tiempo(self):
        print(f"Tardó {self.tiempo} minutos.")


class LavArtesanal(Lavadero):
    """Lavadero artesanal, tarda 1 min cada 5 de suciedad, y cobra personas * min * costo"""

    def __init__(self, costo, personas):
        self.costo = costo
        self.personas = personas

        print(f"Se creó el lavadero.")

    def calcular_precio(self, vehiculo):
        tiempo = self.calcular_tiempo(vehiculo)
        total = self.costo * tiempo * self.personas

        print(f"Salió ${total}.")
        print(f"Tardó {tiempo} minutos.")

    def calcular_tiempo(self, vehiculo):
        """Se estima que se tarda un minuto por cada 5 unidades de suciedad del vehículo"""
        suciedad = vehiculo.get_suciedad()
        minutos = 0

        while suciedad > 0:
            suciedad -= 5
            minutos += 1

        return minutos
