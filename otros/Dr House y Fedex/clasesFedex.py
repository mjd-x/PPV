class envio:
    def __init__(self,id, ciudadOrigen,paisOrigen,ciudadDestino, paisDestino, peso, precioBase):
        self.id=id
        self.ciudadOrigen=ciudadOrigen
        self.paisOrigen=paisOrigen
        self.ciudadDestino=ciudadDestino
        self.paisDestino=paisDestino
        self.peso=peso
        self.precioBase=precioBase
        self.impuestos=[]
        self.categoria=[]
        self.recargo=[]
        self.sumaRecargos=0
        self.sumaImpuestos=0
        self.precioTotal=0

class impuesto:
    def __init__(self,porcentaje, tipo):
        self.valor=0
        self.porcentaje=porcentaje
        self.tipo=tipo
    def calcular(self,envio):
        self.tipo.calcular(self,envio)
#CLASES QUE HEREDAN DE IMPUESTO A FIN DE CALCULAR POLIMORFICAMENTE EL VALOR DEL MISMO
class iva(impuesto):
    def calcular(self,envio):
        self.valor=(envio.precioBase+envio.sumaRecargos)*self.porcentaje

class multicategoria(impuesto):
    def calcular(self,envio):
        if len(envio.categoria)>=3:
            self.valor=(envio.precioBase+envio.sumaRecargos)*self.porcentaje

class aduanero(impuesto):
    def calcular(self,envio):
        if envio.paisOrigen!=envio.paisDestino:
            self.valor=(envio.precioBase+envio.sumaRecargos)*self.porcentaje

class paridad(impuesto):
    def calcular(self,envio):
        if envio.precioBase%2==0:
            self.valor=(envio.precioBase+envio.sumaRecargos)*self.porcentaje

class recargo:
    #valorReferencia se refiere al procentaje, diccionario con porcentajes, suma fija que modifica el precio segun el tipo de recargo
    def __init__(self,valorReferencia,tipo):
        self.valor=0
        self.valorReferecia=valorReferencia
        self.tipo=tipo
    def calcular(self,envio):
        self.tipo.calcular(self,envio)

#CLASES QUE HEREDAN DE RECARGO A FIN DE CALCULAR POLIMORFICAMENTE EL VALOR DEL MISMO
class categorico(recargo):
    def calcular(self,envio):
        for i in range(0,len(envio.categoria)):
            self.valor=self.valor+envio.precioBase*self.valorReferecia.get(envio.categoria[i])

class sobrepeso(recargo):
    #Tambien se podria implementar usando un diccionario de datos que determine valores segun el peso
    def calcular(self,envio):
        if envio.peso>1:
            self.valor=self.valor+int(envio.peso*self.valorReferecia)

class arbitrario(recargo):
    def calcular(self,envio):
        self.valor=self.valor+self.valorReferecia