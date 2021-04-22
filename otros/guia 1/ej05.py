import math


def coordenadas():
    punto = input('Por favor, ingrese el punto en formato x,y : ')
    punto = punto.split(',')
    punto[0] = int(punto[0])
    punto[1] = int(punto[1])
    distancia = math.sqrt(punto[0]**2 + punto[1]**2)
    print('La distancia al origen del punto ({},{}) es: {}'.format(
        punto[0], punto[1], distancia))


coordenadas()
