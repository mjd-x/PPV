from os import system
import datetime
dicCategorias = {
    'tecnologia': 0.1,
    'libros': 0.2,
    'musica': 0.3
}

class FedeX():
    def __init__(self):
        self.envios = []

    def cargar_envio(self, envio):
        self.envios.append(envio)

    def listar_envios(self):
        for envio in self.envios:
            print('El codigo {} va hacia {}'.format(envio.codigo,envio.ciudadD) )

    def borrar_envio(self, codigo):
        self.envios.pop(codigo)

    def listar_Internacionales(self):
        for envio in self.envios:
            if envio.paisO != envio.paisD:
                print('El envio {} va desde {} a {}'.format(envio.codigo, envio.ciudadO, envio.ciudadD))

    def conocer_precio(self, codigo):
        for envio in self.envios:
            if envio.codigo == codigo:
                total = envio.pBase + envio.recargo + envio.imp
                print('El precio por el envio es {}, mas {} de recargos, mas {} de impuestos. Total {}'.format(envio.pBase, envio.recargo, envio.imp, total))


    def a_perderse(self):
        menor = 999999
        codigo = 0
        ciudadO = "origen"
        ciudadD = "Destino"
        for envio in self.envios:
            total = envio.pBase + envio.recargo + envio.imp
            if total < menor:
                menor = total
                codigo = envio.codigo
                ciudadO = envio.ciudadO
                ciudadD = envio.ciudadD
        print('El propicio a perder es el envio con codigo {} que va de {} a {}'.format(codigo, ciudadO, ciudadD))


class Envio():
    def __init__(self, codigo, ciudadO, paisO, ciudadD, paisD, peso, pBase, categorias):
        system("cls")
        self.codigo = codigo
        self.ciudadO = ciudadO
        self.paisO = paisO
        self.ciudadD = ciudadD
        self.paisD = paisD
        self.peso = peso
        self.pBase = pBase
        self.categorias = categorias
        self.impuesto = {}
        self.recargo = 0
        self.imp = 0

    def recargos(self):
        for categoria in self.categorias:
            coeficiente = dicCategorias.get(categoria)
            self.recargo += self.pBase*coeficiente
        if self.peso > 1 :
            self.recargo += 80
        if 'Friday' == datetime.datetime.today().strftime('%A'):
            self.recargo += 50

    def impuestos(self):
        self.impuesto['IVA'] = self.pBase * 1.2
        self.imp += self.pBase * 1.2
        if len(self.categorias) > 3:
            self.impuesto['Multicategoria'] = self.pBase * 1.01
            self.imp += self.pBase * 1.01
        if self.paisO != self.paisD:
            self.impuesto['Aduanero'] = self.pBase * 1.5
            self.imp += self.pBase * 1.5
        if (self.pBase % 2) == 0:
            self.impuesto['Ley de paridad'] = self.pBase * 1.05
            self.imp += self.pBase * 1.05


