import clasesFedex

#VARIABLE GLOBAL CON LAS DIFERENTES CATEGORIAS Y EL PORCENTAJE DE RECARGO
diccCategorias={"tecnologia":0.1,"libro":0.2,"musica":0.3}
#LISTA DE TODOS LOS RECARGOS QUE SE LE DEBEN APLICAR A UN ENVIO
recargos=[clasesFedex.recargo(diccCategorias,clasesFedex.categorico),clasesFedex.recargo(80,clasesFedex.sobrepeso),clasesFedex.recargo(80,clasesFedex.arbitrario)]
#LISTA DE TODOS LOS IMPUESTOS QUE SE LE DEBEN APLICAR A UN ENVIO
impuestos=[clasesFedex.impuesto(0.2,clasesFedex.iva),clasesFedex.impuesto(0.01,clasesFedex.multicategoria),clasesFedex.impuesto(0.5,clasesFedex.aduanero),clasesFedex.impuesto(0.05,clasesFedex.paridad)]
#LISTA DE TODOS LOS ENVIOS, SIMULARIA LA BASE DE DATOS
bdEnvios=[]

#FUNCIONES PARA CADA UNA DE LAS FUNCIONALIDADES DEL SISTEMA
def calcularRecargos(envio):
    for i in range (0,len(envio.recargo)):
        envio.recargo[i].calcular(envio)

def calcularImpuestos(envio):
    for i in range (0,len(envio.impuestos)):
        envio.impuestos[i].calcular(envio)

def cargarEnvio():
    print("********************ALTA ENVIO************************")
    id = int(input("Ingrese el numero de envío: "))
    print("NOTA: para las ciudades y paises ingrese cadenas de caracteres")
    ciudadOrigen = input("Ingrese la ciudad de origen: ")
    print("NOTA: Si el pais de origen o destino es Argentina, ingrese arg")
    paisOrigen = input("Ingrese el pais de origen: ")
    ciudadDestino = input("Ingrese la ciudad de destino: ")
    paisDestino = input("Ingrese el pais de destino: ")
    peso = float(input("Ingrese el peso: "))
    precioBase = float(input("Ingrese precio base: "))
    cantCategorias = int(input("Ingrese la cantidad de categorias: "))
    nuevoEnvio = clasesFedex.envio(id,ciudadOrigen, paisOrigen, ciudadDestino, paisDestino, peso, precioBase)
    print(f"NOTA: categorias disponibles: {diccCategorias.keys()}")
    for i in range(0,cantCategorias):
        nuevoEnvio.categoria.append(input("Ingrese una de las categorías: "))
    nuevoEnvio.recargo=recargos
    calcularRecargos(nuevoEnvio)
    for i in range(0, len(nuevoEnvio.recargo)):
        nuevoEnvio.sumaRecargos = nuevoEnvio.sumaRecargos + nuevoEnvio.recargo[i].valor
    nuevoEnvio.impuestos=impuestos
    calcularImpuestos(nuevoEnvio)
    for i in range(0, len(nuevoEnvio.impuestos)):
        nuevoEnvio.sumaImpuestos = nuevoEnvio.sumaImpuestos + nuevoEnvio.impuestos[i].valor
    nuevoEnvio.precioTotal=nuevoEnvio.precioBase+nuevoEnvio.sumaRecargos+nuevoEnvio.sumaImpuestos
    bdEnvios.append(nuevoEnvio)

def listarEnvio(envio):
    print("----------------ENVIO------------------")
    print(f"Envío: {envio.id}")
    print(f"Ciudad de origen: {envio.ciudadOrigen}")
    print(f"Pais de origen: {envio.paisOrigen}")
    print(f"Ciudad de destino: {envio.ciudadDestino}")
    print(f"Pais de destino: {envio.paisDestino}")
    print(f"Peso: {envio.peso}")
    print(f"Precio base: {envio.precioBase}")
    print(f"Categoria: {envio.categoria}")
    print(f"Total Recargos: {envio.sumaRecargos}")
    print(f"Total Impuestos: {envio.sumaImpuestos}")
    print(f"Precio Total: {envio.precioTotal}")

def listarTodosEnvios():
    print("*****************LISTADO ENVIOS **********************")
    for i in range(0, len(bdEnvios)):
        listarEnvio(bdEnvios[i])

def borrarEnvio():
    print("*****************BORRADO ENVIO **********************")
    id = int(input("Ingrese el numero de envío que desea borrar: "))
    i=0
    while i<len(bdEnvios):
        if bdEnvios[i].id==id:
            bdEnvios.pop(i)
            print("Envio Borrado")
        else:
            i=i+1

def listarInternacionales():
    print("*****************LISTADO INTERNACIONALES**********************")
    for i in range(0,len(bdEnvios)):
        if bdEnvios[i].paisDestino!="arg":
            listarEnvio(bdEnvios[i])

def conocerPrecio():
    print("*****************PRECIO ENVIO**********************")
    id = int(input("Ingrese el numero de envío que quiere saber el precio: "))
    for i in range(0,len(bdEnvios)):
        if bdEnvios[i].id==id:
            print(f"Precio total: {bdEnvios[i].precioTotal}")

def propicioPerderse():
    print("*****************ENVIO PROPICIO A PERDERSE**********************")
    min=99999999
    propicioPerderse=0
    for i in range(0,len(bdEnvios)):
        if bdEnvios[i].precioTotal<=min:
            propicioPerderse=i
            min=bdEnvios[i].precioTotal
    listarEnvio(bdEnvios[propicioPerderse])

#IMPLEMENTACION DE LAS FUNCIONALIDADES
print("********************SISTEMA ABM************************")
print("1) Cargar nuevo envío")
print("2) Listar envíos")
print("3) Borrar envíos")
print("4) Listar envíos internacionales")
print("5) Conocer el precio de un envío")
print("6) Conocer el envío “propicio a perderse”")

opcion = int(input("Ingrese la opción deseada (0 para salir):"))
print("********************************************")
while opcion != 0:
    if opcion == 1:
        cargarEnvio()
    if opcion == 2:
        listarTodosEnvios()
    if opcion == 3:
        borrarEnvio()
    if opcion == 4:
        listarInternacionales()
    if opcion == 5:
        conocerPrecio()
    if opcion == 6:
        propicioPerderse()
    print("***************************************")
    print("1) Cargar nuevo envío")
    print("2) Listar envíos")
    print("3) Borrar envíos")
    print("4) Listar envíos internacionales")
    print("5) Conocer el precio de un envío")
    print("6) Conocer el envío “propicio a perderse”")

    opcion = int(input("Ingrese la opción deseada (0 para salir):"))
    print("***************************************")

