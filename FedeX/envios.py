class Fedex:
    """sistema gral en donde tengo listados todos los envios. reemplazaria a la DB"""
    def __init__(self):
        self.envios = []  # todos los envios existentes
        self.impuestos = []  # todos los impuestos existentes
        self.recargos = []  # todos los recargos existentes

    def agregar_impuesto(self, impuesto):
        self.impuestos.append(impuesto)

    def borrar_impuesto(self, imp):
        cont = 0  # para poder usar la funcion pop necesito el indice, pero itero en el for por objeto
        for impuesto in self.impuestos:  # itero objetos envio en la lista
            if impuesto == imp:
                self.impuestos.pop(cont)  # si es el codigo que busco, lo saco de la lista por indice
            else:
                cont += 1  # si no es el codigo que busco, sigue iterando

    def calcular_impuestos(self, envio):
        for impuesto in self.impuestos:
            impuesto.aplicar_impuesto(envio)  # aplica impuesto
            envio.impuestos.append(impuesto)  # lo agrega a la lista de impuestos que se aplicaron al envio
            # definicion de condicion (si se debe aplicar o no) en el metodo de cada impuesto

    def agregar_recargo(self, recargo):
        self.recargos.append(recargo)

    def borrar_recargo(self, rec):
        cont = 0  # para poder usar la funcion pop necesito el indice, pero itero en el for por objeto
        for recargo in self.recargos:  # itero objetos envio en la lista
            if recargo == rec:
                self.recargos.pop(cont)  # si es el codigo que busco, lo saco de la lista por indice
            else:
                cont += 1  # si no es el codigo que busco, sigue iterando

    def calcular_recargos(self, envio):
        for recargo in self.recargos:
            recargo.aplicar_recargo(envio)  # aplica recargo
            envio.recargos.append(recargo)  # lo agrega a la lista de recargos que se aplicaron al envio
            # definicion de condicion (si se debe aplicar o no) en el metodo de cada recargo

    def agregar_envio(self, envio):
        """carga nuevo envio al sistema"""
        self.calcular_impuestos(envio)  # calcula impuestos
        self.calcular_recargos(envio)  # calcula recargos
        self.envios.append(envio)
        print("Envío cargado.\n")

    def borrar_envio(self, cod):
        """borra un envio existente del sistema"""
        cont = 0  # para poder usar la funcion pop necesito el indice, pero itero en el for por objeto
        for envio in self.envios:  # itero objetos envio en la lista
            if envio.codigo == cod:
                self.envios.pop(cont)  # si es el codigo que busco, lo saco de la lista por indice
            else:
                cont += 1  # si no es el codigo que busco, sigue iterando

    def listar_envios(self):
        """Imprime informacion de todos los envios en el sistema"""
        for envio in self.envios:
            print(f"\n---Envío {envio.codigo}:---")
            print(f"\tOrigen: {envio.origen[0]}, {envio.origen[1]}")
            print(f"\tDestino: {envio.destino[0]}, {envio.destino[1]}")
            print(f"\tPeso: {envio.peso}")
            print(f"\tPrecio total: {envio.precioT}\n")

    def listar_internacionales(self):
        """Imprime informacion de envios que su destino no es en el pais de origen"""
        for envio in self.envios:
            if envio.origen[0] != envio.destino[0]:
                print(f"\n---Envío {envio.codigo}:---")
                print(f"\tOrigen: {envio.origen[0]}, {envio.origen[1]}")
                print(f"\tDestino: {envio.destino[0]}, {envio.destino[1]}")
                print(f"\tPeso: {envio.peso}")
                print(f"\tPrecio total: {envio.precioT}\n")

    def buscar_envio(self, cod):
        """Recibe codigo de envio y lo busca, devuelve el envio que es o imprime error si no esta"""
        for envio in self.envios:
            if envio.codigo == cod:
                return envio
        else:
            print("No se encontró el envío.\n")

    def propicio_perderse(self):
        """envio que tiene el precio bruto más barato de todos"""
        menor = min(self.envios, key=lambda envio: envio.precioT)
        print(f"El envío propicio a perderse es {menor.codigo}.\n")


class Envio:
    """información básica, éstas son: lugar de origen (ciudad y país), lugar de destino (idem), peso en kilogramos,
       precio base, categorías que brindan información del contenido y varios impuestos asociados"""
    def __init__(self, codigo, origen, destino, peso, categorias, precioB):
        self.codigo = int(codigo)
        self.origen = origen  # lista tipo [ciudad, pais]
        self.destino = destino  # lista tipo [ciudad, pais]
        self.peso = float(peso)
        self.precioB = float(precioB)
        self.categorias = categorias

        self.precioT = float(precioB)  # le asigno el precio base al precio total, luego se aplican los impuestos

        self.impuestos = []  # impuestos que aplican al envip
        self.recargos = []  # recargos que aplican al envio


class Impuesto:
    """clase base para poder agregar mas impuestos a futuro y que puedan cambiar el metodo si es necesario
       Los impuestos se aplican sobre el precio base sumado a todos los cargos extra."""
    def __init__(self, porcentaje):
        self.porcentaje = float(porcentaje/100)

    def aplicar_impuesto(self, envio):
        envio.precioT += (envio.precioB * self.porcentaje)  # le suma el porcentaje al precio total del envio


class Multicategoria(Impuesto):
    """1% del precio neto, se aplica cuando el envío tiene más de 3 categorías"""
    def aplicar_impuesto(self, envio):
        if len(envio.categorias) > 3:
            envio.precioT += (envio.precioB * self.porcentaje)


class Aduanero(Impuesto):
    """50%, pero sólo cuando el envío es internacional"""
    def aplicar_impuesto(self, envio):
        if envio.origen[0] != envio.destino[0]:
            envio.precioT += (envio.precioB * self.porcentaje)


class Paridad(Impuesto):
    """5% sólo si tiene precio base es par."""
    def aplicar_impuesto(self, envio):
        if envio.precioB % 2 == 0:
            envio.precioT += (envio.precioB * self.porcentaje)


class Recargo:
    """Existen recargos extra que aumentan el precio de envío de acuerdo con el contenido.
       Por lo tanto, si cumple o no con ciertas características, se aplican determinados recargos."""
    def __init__(self, valor):
        self.valor = valor

    def aplicar_recargo(self, envio):
        envio.precioT += self.valor


class Categorico(Recargo):
    """Si el envío tiene una categoría determinada, se computa un porcentaje dado del precio base.
       Por ejemplo 10% para la tecnología"""
    def aplicar_recargo(self, envio):
        for categoria in envio.categorias:
            if categoria == "tecnologia":
                envio.precioT += envio.precioB * (self.valor / 100)


class Sobrepeso(Recargo):
    """Si el peso es mayor a un peso dado (1kg) se le suma $80."""
    def aplicar_recargo(self, envio):
        if envio.peso > 1:
            envio.precioT += self.valor


FedeX = Fedex()  # instancio la "DB", mejor aca que en el main

# Impuestos existentes, los instancio y agrego a la "DB". mejor aca que en el main
IVA = Impuesto(20)  # no tiene ningun criterio de aplicacion. impuesto "comun"
FedeX.agregar_impuesto(IVA)
multicategoria = Multicategoria(1)
FedeX.agregar_impuesto(multicategoria)
aduanero = Aduanero(50)
FedeX.agregar_impuesto(aduanero)
paridad = Paridad(5)
FedeX.agregar_impuesto(paridad)

# Recargos existentes, los instancio y agrego a la "DB". mejor aca que en el main
categorico = Categorico(10)
FedeX.agregar_recargo(categorico)
sobrepeso = Sobrepeso(80)
FedeX.agregar_recargo(sobrepeso)
arbitrario = Recargo(50)
FedeX.agregar_recargo(arbitrario)
