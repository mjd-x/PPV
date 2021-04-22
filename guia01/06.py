import sys
import productos

def menu(): # a
    """Imprime las opciones y recibe el numero, lleva a esa funcion"""

    print("1) Buscar producto")
    print("2) Ingresar nueva factura")
    print("3) Ingresar nuevo producto al catálogo")
    print("4) Salir")

    switch = {
        1: buscar,
        2: factura,
        3: producto,
        4: sys.exit
             }

    opc = int(input("\nSeleccione la opcion: "))
    switch.get(opc, "Opción incorrecta")()


def buscar():  # c
    """Toma id del producto y se la pasa a buscar(), si recibe el producto imprime los datos y vuelve al menu"""
    id = int(input("Ingrese el código de producto: "))
    producto = productos.buscar(id)

    print(f"Código: {producto['codigo']}, "
          f"Descripción: {producto['desc']}, "
          f"Precio: {producto['precio']}")

    print("\n\n")
    menu()


def factura():  # d
    """Invoca a factura y vuelve al menu"""
    productos.factura()

    print("\n\n")
    menu()


def producto():
    catalogo = productos.agregar()
    print("Catálogo actualizado.")
    for _ in catalogo:
        print("Código: {} — Descripción: {} — Precio: {}".format(_['codigo'], _['desc'], _['precio']))

    print("\n\n")
    menu()


menu()