from os import system
from envios import *
fedex = FedeX()


def cargar_envio():
    system("cls")
    codigo = int(input('ingrese el codigo: '))
    ciudadO = input('ingrese ciudad de origen: ')
    paisO = input('ingrese pais de origen: ')
    ciudadD = input('ingrese ciudad de destino: ')
    paisD = input('ingrese pais de destino: ')
    peso = float(input('ingrese peso: '))
    pBase = float(input('ingrese precio base: '))
    categorias = []
    op = input('desea cargar categorias?:[S/N]').lower()
    while op != 'n':
        categorias.append(input('Ingrese el nombre de la categoria'))
        op = input('desea cargar categorias?:[S/N]').lower()
    envio = Envio(codigo, ciudadO, paisO, ciudadD, paisD, peso, pBase, categorias)
    envio.recargos()
    envio.impuestos()
    fedex.cargar_envio(envio)


def listar_envios():
    fedex.listar_envios()


def borrar_envio():
    codigo = (int(input('ingrese el codigo del envio a borrar')) - 1)
    fedex.borrar_envio(codigo)


def listar_internacionales():
    fedex.listar_Internacionales()


def conocer_precio():
    codigo = int(input('ingrese el codigo del envio a borrar'))
    fedex.conocer_precio(codigo)

def a_perderse():
    fedex.a_perderse()

opcion = 99
while opcion != 0:
    print('Bienvenido al sistema de FedeX!')
    print('Por favor, elija la opcion:\n')
    print('1) Cargar un nuevo envio')
    print('2) Listar todos los envios')
    print('3) Borrar un envio')
    print('4) Listar todos los envios internacionales')
    print('5) Conocer el precio de un envio')
    print('6) Conocer el envio "propicio a perderse"')
    opcion = int(input('\nIngrese la opcion deseada (0 para salir): '))
    if opcion == 1:
        system("cls")
        cargar_envio()

    elif opcion == 2:
        listar_envios()
    elif opcion == 3:
        borrar_envio()
    elif opcion == 4:
        listar_internacionales()
    elif opcion == 5:
        conocer_precio()
    elif opcion == 6:
        a_perderse()
    elif opcion != 0:
        opcion = int(input('\nIngrese la opcion deseada (0 para salir): '))
    else:
        print('Adios!')


