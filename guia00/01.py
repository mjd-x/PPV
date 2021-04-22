def get_range():
    """reciba como parámetros el inicio y fin (inclusive) de un rango numérico.
    a. divisibles por 7 pero no sean divisibles por 5
    b. separados por coma"""

    start = int(input("Ingrese el número de inicio: "))
    stop = int(input("Ingrese el número de fin: "))

    for _ in range(start, stop + 1):  # a
        if _ %7 == 0 and _ %5 != 0:
            print(_)

    for _ in range(start, stop + 1):  # b
        if _ % 7 == 0 and _ % 5 != 0:
            print(_, end=',')


get_range()
