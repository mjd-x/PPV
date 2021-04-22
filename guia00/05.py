from math import pi as pi


def circulo(radio):
    """recibe el radio de un circulo y devuelve una tupla con el perímetro y el área"""

    perim = 2 * pi * radio
    area = pi * radio * radio

    return (perim, area)


inp = float(input("Ingrese el radio: "))
print(circulo(inp))
