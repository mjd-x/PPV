class Maquina:
    def __init__(self,bandejaIngredientes):
        self.bandejaIngredientes=bandejaIngredientes
        self.recaudacion=0
        self.log=[]
        #estado: 1 en servicio, 0 necesita alguna recarga
        self.estado=1

    def prepararBebida(self,bebida):
        ingredientes=bebida.ingredientes.keys()
        flag=0
        for ing in ingredientes:
            if bandejaCompletaIngredientes[ing]<bebida.ingredientes[ing]:
                print(f"no se puede preparar, falta {ing}")
                #se detecta que falta un producto así que se deja marcado que esta necesitando alguna recarga
                self.estado=0
                flag=1
            else:
                self.bandejaIngredientes[ing]=self.bandejaIngredientes[ing]-bebida.ingredientes[ing]
        if flag!=1:
            self.recaudacion=self.recaudacion+bebida.valor
            self.log.append(bebida.tipo)

    def comprarBebida(self,dineroIn,bebida):
        if dineroIn>=listaPrecio[bebida.tipo]:
            self.prepararBebida(bebida)
        else:
            print("Ingrese mas dinero")

    def consultarReabastecimiento (self,limites):
        ing=limites.keys()
        for i in ing:
            if self.bandejaIngredientes[i]<=limites[i]:
                print(f"debe recargar {i}")
                self.estado=0
            else:
                print(f"el nivel de {i} esta OK")

#esta clase podría no existir, ya que todas las funciones se manejan con un diccionario
class Bebida:
    def __init__(self, tipo, ingredientes,valor):
        self.ingredientes=ingredientes
        self.tipo=tipo
        self.valor=valor

#-------------------------------------
#IMPLEMENTACION
#se crean los diccionarios de referencia, a fin de traducir lo ingresado por el usuario
codigoBebidas={"cafe":1,"granizadoCremoso":2}
codigoIngredientes={"Leche":1,"Leche Descremada":2,"Azucar":3,"Azúcar Morena":4,"Cafe Torrado Suave":5,"Cafe Torrado Intenso":6,"Canela Molida":7,"Crema":8}
#Es una especie de libro con las proporciones de cada bebida
libroBebidas={1:{5:20}, 2:{1:280,4:100,5:10,7:2}}
#recarga inicial para cada maquina expendedora
bandejaCompletaIngredientes={1:500,2:500,3:500,4:500,5:500,6:500,7:500,8:500}
#los limites que considera el usuario que no se deben disminuir
limitesIngredientes={1:100,2:100,3:100,4:100,5:100,6:100,7:100,8:100}
listaPrecio={1:20,2:30}
#instancia de las maquinas que tiene el sistema, la maquina 2 y 3 simulan las maquinas conectadas a internet
maquina=Maquina(bandejaCompletaIngredientes)
maquina2=Maquina(bandejaCompletaIngredientes)
#se le asignan valores arbitrarios a la maquina 2 a fin de comprobar el correcto funcionamiento de las funciones
maquina2.recaudacion=50
maquina2.log=[2,2,2,2,2,2]
maquina3=Maquina(bandejaCompletaIngredientes)
#simula ser la BD con todas las maquinas expendedoras
listadoMaquinas=[maquina,maquina2,maquina3]

#-----------------------------------------

#FUNCIONES PARA EL MENU
def comprar(maquina,codigoBebidas,libroBebidas,listaPrecio):
    dinero=float(input(f"ingrese el dinero que tiene, la lista de precios es {listaPrecio}, para los codigos{codigoBebidas}"))
    nombre=input(f"ingrese la bebida que quiere de las siguientes opciones: {codigoBebidas.keys()}")
    codBeb=codigoBebidas.get(nombre,"no existe el producto")
    if nombre in codigoBebidas:
        bebida=Bebida(codBeb,libroBebidas.get(codBeb),listaPrecio.get(codBeb))
        maquina.comprarBebida(dinero,bebida)
    else:
        print("no existe el producto")

def consultaNivelesIngredientes(maquina):
    #consulta niveles ingredientes
    print(maquina.bandejaIngredientes.items())

def consultaReabastecer(maquina):
    #consulta reabastecimiento
    maquina.consultarReabastecimiento(limitesIngredientes)

def consultaRecaudacion(maquina):
    print(maquina.recaudacion)

def mayorCantidad(maquina, codigoBebidas):
    cantidades=[]
    codBeb=[]
    nombreBeb=[]
    for nombre, cod in codigoBebidas.items():
        codBeb.append(cod)
        nombreBeb.append(nombre)
    for i in range(0,len(codBeb)):
        cantidades.append(0)
    for i in range(0,len(maquina.log)):
        cantidades[maquina.log[i]-1]+=1
    print(f"el producto mas vendido es {nombreBeb[cantidades.index(max(cantidades))]}")

def cantMaqReabastecer(listadoMaquinas,limites):
    cant=0
    ing = limites.keys()
    for i in range(0,len(listadoMaquinas)):
        for c in ing:
            if listadoMaquinas[i].bandejaIngredientes[c] <= limites[c]:
                listadoMaquinas[i].estado=0
                cant+=1
    print(f"se deben recargar {cant} maquinas")

def recaudacionTotal(listadoMaquinas):
    recaudacionTotal=0
    for i in range(0,len(listadoMaquinas)):
        recaudacionTotal+=listadoMaquinas[i].recaudacion
    print(f"la recaudacion total es {recaudacionTotal}")

def bebidaFavorita(listadoMaquinas):
    #se instancia un objeto a fin de asignarle un log con todas las operaciones realizadas
    maq=Maquina(bandejaCompletaIngredientes)
    for i in range(0,len(listadoMaquinas)):
        maq.log+=listadoMaquinas[i].log
    mayorCantidad(maq,codigoBebidas)

#MENU

opcion=99
while opcion != 0:
    print("***************************************")
    print("1) Preparar bebida")
    print("2) Consultar si se necesita reabastecimiento")
    print("3) Consutlar recaudacion")
    print("4) Consultar bebida mas servida")
    print("5) Consultar cantidad de maquinas a reabastecer")
    print("6) Recaudacion total")
    print("7) Bebida Favorita")
    opcion = int(input("Ingrese la opción deseada (0 para salir):"))
    print("********************************************")
    if opcion == 1:
        comprar(maquina,codigoBebidas,libroBebidas,listaPrecio)
    if opcion == 2:
        consultaNivelesIngredientes(maquina)
        consultaReabastecer(maquina)
    if opcion == 3:
        consultaRecaudacion(maquina)
    if opcion == 4:
        mayorCantidad(maquina,codigoBebidas)
    if opcion == 5:
        cantMaqReabastecer(listadoMaquinas,limitesIngredientes)
    if opcion == 6:
        recaudacionTotal(listadoMaquinas)
    if opcion == 7:
        bebidaFavorita(listadoMaquinas)