import math
import sys


def coordenada():
    """Toma un punto en formato x,y e imprime su distancia al origen llamando a calcula()"""

    p = input("Ingrese el punto en formato x,y: ")

    coord = p.split(",")
    x = int(coord[0])
    y = int(coord[1])

    while True:
        if x == 0 and y == 0:
            print("Fin del programa")
            sys.exit(0)

        else:
            calcula(x, y)
            p = input("Ingrese el punto en formato x,y: ")

            coord = p.split(",")
            x = int(coord[0])
            y = int(coord[1])


def calcula(x, y):
    """recibe los valores x, y de la coordenada e imprime la distancia al origen"""

    result = math.sqrt(x ** 2 + y ** 2)
    print(f"La distancia al origen del punto {(x,y)} es: {result}\n")


coordenada()
