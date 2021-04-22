from os import system
import productos


def menu():
    opcion = 0
    while opcion != 4:
        print('1) Buscar producto')
        print('2) Ingresar nueva factura')
        print('3) Ingresar nuevo producto')
        print('4) Salir')
        opcion = int(input('Por favor, seleccione una opcion:\n'))
        if opcion == 1:
            system('cls')
            codigo = int(input("Buscar por codigo: "))
            productos.buscar(codigo)

        if opcion == 2:
            system('cls')
            print("Ingresar nueva factura")
            productos.nuevaFactura()

        if opcion == 3:
            system('cls')
            print('Cargar nuevo producto')
            productos.cargarProducto()


menu()
