class Maquina:
    def __init__(self, leche, lecheD, azucar, azucarM, cafeS, cafeI, canela, crema, recipientes):
        """Ingredientes posibles en la maquina +  recipientes + recaudacion + bebidas que sirvio
           el agua es ilimitada"""

        self.ingredientes = \
            {
                'leche': int(leche),
                'lecheDesc': int(lecheD),
                'azucar': int(azucar),
                'azucarM': int(azucarM),
                'cafeS': int(cafeS),
                'cafeI': int(cafeI),
                'canela': int(canela),
                'crema': int(crema)
            }  # acceso por llaves porque una bebida no usa todos los ingredientes
               # evita tener que ingresar "0" para cada ingrediente que no use la bebida
               # evita tener que restarle 0 a ingredientes que no se usaron para esa bebida

        self.recipientes = int(recipientes)

        self.recaudacion = 0.00
        self.bebidasServidas = []

    def preparar_bebida(self, bebida):
        """resta de los ingredientes, si no alcanza no prepara
           verifica que haya recipientes para usar, si no alcanzan no prepara"""

        if self.recipientes == 0:  # no hay recipientes
            print("No se preparó la bebida porque no hay recipientes")
            return None

        else:
            ingrediente = list(bebida.composicion.keys())
            proporcion = list(bebida.composicion.values())  # toma ingredientes que tiene esa bebida

            for i in range(len(ingrediente)):
                if self.ingredientes[(ingrediente[i])] - proporcion[i] < 0:
                    print("No se preparó la bebida porque hay ingredientes suficientes")
                    return None

                else:
                    self.ingredientes[(ingrediente[i])] -= proporcion[i]  # resta a la maquina los ingreds

            self.recaudacion += bebida.precio  # pago
            self.bebidasServidas.append(bebida.nombre)  # porque necesito saber cual bebida es popular

            print("Bebida lista")

    def consultar_ingredientes(self):
        for value in self.ingredientes.values():  # itera por todos los valores del diccionario ingredientes
            if value == 0:
                print("La maquina necesita reabastecimiento")
                break  # con que falte de 1 ingrediente ya hay que reabastecer?

    def consultar_recaudacion(self):
        """Se puede consultar la recaudacion acumulada"""
        print(f"Se recaudaron ${self.recaudacion}")

    def bebidas_servidas(self):
        """Se puede consultar la cant de bebidas servidas"""
        print(f"Se sirvieron {len(self.bebidasServidas)} bebidas")

    def bebida_popular(self):
        """cual bebida fue servida mas veces por la maquina"""
        bebidas = [[x,self.bebidasServidas.count(x)] for x in self.bebidasServidas]  # cuenta cuantas veces se sirvio
        return bebidas[0][0]  # devuelve la bebida que se sirvio mas veces en la maquina


class Bebida:
    def __init__(self):
        """Cada bebida tiene su propia "receta", usa ciertas proporciones de algunos ingredientes"""
        self.composicion = {}  # ingredientes y proporcion de cada uno
        self.nombre = input("Ingrese el nombre: ")  # para usar en bebida_popular, forma de distinguir entre bebidas

        print("Ingredientes posibles:")
        print("\tleche\n\tleche descremada (lecheD)\n\tazucar\n\tazucar morena (azucarM)\n\tCafe torrado suave (cafeS)")
        print("\tCafe torrado intenso (cafeI)\n\tcanela\n\tcrema")

        ing = input("Ingrese ingrediente ('fin' para terminar): ")
        while ing != "fin":
            cant = int(input("Ingrese cantidad: "))
            self.composicion[ing] = cant  # como diccionario para no tener que poner "0" en los ingredientes
                                          # que no se van a usar, acceso por llave

            ing = input("Ingrese ingrediente ('fin' para terminar): ")

        self.precio = float(input("Ingrese el precio: "))  # cuanto sale la bebida


class Red:
    def __init__(self):
        """Las maquinas se encuentran conectadas a una red informatica(...) se puede saber su estado"""
        self.maquinas = []

    def agregar(self, Maquina):
        """agregar una maquina a la red"""
        self.maquinas.append(Maquina)

    def reabastecimiento(self):
        """verificar si las maquinas de la red se tienen que reabastecer"""
        for maquina in self.maquinas:
            maquina.consultar_ingredientes()

    def calcular_recaudacion(self):
        """Devuelve recaudacion acumulada por todas las maquinas de la red"""
        recaud = 0.00

        for maquina in self.maquinas:
            recaud += maquina.recaudacion  # agrega recaudacion de cada maquina de la red

        print(f"Se recaudó en total ${recaud}")

    def bebida_popular(self):
        """bebida mas servida entre todas las maquinas de la red"""
        lista = []

        for maquina in self.maquinas:
            lista.append(maquina.bebida_popular())  # agrega bebida popular por maquina

        bebidas = [[x, lista.count(x)] for x in lista]  # cuenta cuantas veces esta cada bebida en la lista
        print(f"La bebida popular del mercado es {bebidas[0][0]}")  # devuelve la mas pedida
