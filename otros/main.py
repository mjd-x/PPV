class Pais:

    def __init__(self, nombre):
        self.nombre = nombre
        self.ciudades = []

    def addCiudad(self, nombre):
        self.ciudades.append(nombre)

class Ciudad:

    def __init__(self,nombre):
        self.nombre = nombre

class Categoria:

    def __init__(self, nombre):
        self.nombre = nombre


class Recargo:

    def __init__(self, nombre):
        self.nombre = nombre

class RecargoPorcentual:
    def __init__(self, nombre, porcentaje):
        self.porcentaje = porcentaje
        Recargo.__init__(self, nombre)


class RecargoMonetario:
    def __init__(self, nombre, monto):
        self.monto = monto
        Recargo.__init__(self, nombre)

class Envio:

    def __init__(self, origen, destino, peso, precioBase):
        self.origen = origen
        self.destino = destino
        self.peso = peso
        self.precioBase = precioBase
        self.categorias = []
        self.recargos = []
        self.impuestos = []

    def addCategoria(self,categoria):
        self.categorias.append(categoria)

    def addRecargo(self,recargo):
        self.recargos.append(recargo)

    def addImpuesto(self,impuesto):
        self.impuestos.append(impuesto)

    def procesarRecargos(self):
        # CONDICIONES DE LOS RECARGOS E IMPUESTOS

        if categoria1 in self.categorias:
            self.addRecargo(recargoCategorico)

        if self.peso > 1:
            self.addRecargo(recargoSobrepeso)

        self.addImpuesto(impIVA)

        if len(self.categorias) >= 3:
            self.addImpuesto(impMulticategoria)


    def calcularImpuestos(self,neto):

        total = 0
        for recargo in self.impuestos:
            total += neto*recargo.porcentaje

        return total

    def calcularRecargos(self):

        neto = self.precioBase
        for recargo in self.recargos:
            if recargo is RecargoPorcentual:
                neto+=self.precioBase*recargo.porcentaje
            if recargo is RecargoMonetario:
                neto+=recargo.monto
        return neto


    def calcularTotal(self):
        neto = self.calcularRecargos()
        total = neto + self.calcularImpuestos(neto)
        return total



    #CREO UN PAIS Y AGREGO CIUDADES

Argentina = Pais('Argentina')
Rosario = Ciudad('Rosario')
Cordoba = Ciudad('Cordoba')
Ushuaia = Ciudad('Ushuaia')
Salta = Ciudad('Salta')

Argentina.addCiudad(Rosario)
Argentina.addCiudad(Cordoba)
Argentina.addCiudad(Ushuaia)
Argentina.addCiudad(Salta)

#CREO CATEGORIAS
categoria1 = Categoria('Tecnologia')
categoria2 = Categoria('Libro')
categoria3 = Categoria('Musica')

#CREO RECARGOS E IMPUESTOS
recargoCategorico = RecargoPorcentual('Recargo categorico',10)
recargoSobrepeso = RecargoMonetario('Recargo por sobrepeso',80)
impIVA = RecargoPorcentual('IVA',21)
impMulticategoria = RecargoPorcentual('Impuesto multicategoria',1)
impAduanero = RecargoPorcentual('Impuesto Aduanero',50)

#CREO ENVIO
envio1 = Envio(Cordoba,Salta,0.5,500)
envio1.addCategoria(categoria1)
envio1.procesarRecargos()
print (envio1.calcularTotal())