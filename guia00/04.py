def separa(cadena):  # a
    """Recibe un string de elementos separados por coma y retorna una lista conteniendo cada elemento"""

    return cadena.split(",")


def separa_tipos(cadena):  # b
    """Mismo pero obteniendo correctamente cada dato según su tipo (numero entero, string, boolean)"""

    lista = cadena.split(",")
    try:
        lista[0] = int(lista[0])

        if lista[2] == "True":
            lista[2] = True
        else:
            lista[2] = False

        return lista

    except:
        return "Algo salió mal"


def separa_lista(lista):  # c
    """Mismo pero recibe una lista de strings y retorna otra lista, como listas con los campos formateados"""

    for _ in range(len(lista)):
        lista[_] = separa_tipos(lista[_])

    return lista


cad = str(input("Ingrese los datos separados por coma: "))
print(separa(cad))

print(separa_tipos(cad))

lis = ["14,pepe,True", "45,juan,False"]
print(separa_lista(lis))