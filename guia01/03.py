import fechas


def is_int(cadena):
    """verifica si un string esta compuesto solamente por enteros"""

    for _ in range(len(cadena)):
        if not cadena[_].isdigit():
            return False
    return True


def is_str(cadena):
    """verifica si un string esta compuesta solamente por letras"""

    for _ in range(len(cadena)):
        if not cadena[_].isalpha():
           return False
    return True


"""toma mes, abreviatura y dias y se los pasa a crear_mes, verificando los datos"""

entrada = input("Ingrese el mes: ")
while not is_str(entrada):
    print("Tipo de dato incorrecto\n")
    entrada = input("Ingrese el mes: ")

mes = entrada

entrada = input("Ingrese la abreviatura: ")
while not is_str(entrada):
    print("Tipo de dato incorrecto\n")
    entrada = input("Ingrese la abreviatura: ")

abv = entrada

entrada = input("Ingrese la cantidad de días: ")
while not is_int(entrada):
    print("Tipo de dato incorrecto\n")
    entrada = input("Ingrese la cantidad de días: ")

dia = entrada

fechas.crear_mes(mes, abv, dia)
