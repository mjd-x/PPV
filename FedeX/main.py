import sys
import envios


def menu():
    """Imprime las opciones y recibe el numero, lleva a esa funcion"""
    print("Bienvenido al sistema de FedeX!")
    print("Por favor, elija una opción: ")

    print("1) Cargar un nuevo envío")
    print("2) Listar todos los pedidos")
    print("3) Borrar un envío")
    print("4) Listar todos los envíos internacionales")
    print("5) Conocer el precio de un envío")
    print("6) Conocer el envío \"propicio a perderse\"")

    switch = {
        0: sys.exit,
        1: cargar,
        2: lista_envios,
        3: borrar,
        4: lista_internacional,
        5: consultar_precio,
        6: perderse
    }

    opc = int(input("\nPor favor, elija la opción deseada (0 para salir): "))
    switch.get(opc, "Opción incorrecta")()


def cargar():
    codigo = input("Ingrese el código: ")
    pais = input("Ingrese el país de origen: ")
    ciudad = input("Ingrese la ciudad de origen: ")
    origen = [ciudad, pais]

    pais = input("Ingrese el país de destino: ")
    ciudad = input("Ingrese la ciudad de destino: ")
    destino = [ciudad, pais]

    peso = input("Ingrese el peso: ")
    precio = input("Ingrese el precio base: ")

    categorias = []
    cat = input("Ingrese las categorías ('fin' para terminar): ")
    while cat != 'fin':
        categorias.append(cat)
        cat = input("Ingrese las categorías del envío ('fin' para terminar): ")

    env = envios.Envio(codigo, origen, destino, peso, categorias, precio)
    envios.FedeX.agregar_envio(env)

    menu()


def lista_envios():
    envios.FedeX.listar_envios()

    menu()  # hago la funcion de nuevo aca para poder volver al menu


def lista_internacional():
    envios.FedeX.listar_internacionales()

    menu()  # hago la funcion de nuevo aca para poder volver al menu


def perderse():
    envios.FedeX.propicio_perderse()

    menu ()  # hago la funcion de nuevo aca para poder volver al menu


def borrar():
    codigo = int(input("Ingrese el código: "))
    envios.FedeX.borrar_envio(codigo)

    menu()


def consultar_precio():
    codigo = int(input("Ingrese el codigo: "))
    envio = envios.FedeX.buscar_envio(codigo)
    print(f"El precio total del envío es ${envio.precioT}.\n")

    menu()


menu()
