def separar(frase):
    lista = frase.split(',')
    lista[0] = int(lista[0])
    lista[1] = str(lista[1])
    lista[2] = bool(lista[2])
    return lista


def listaDeListas(campo):
    resultado = []
    for i in campo:
        resultado.append(separar(i))
    return resultado


print(listaDeListas(["14, Juana perez, True", "16, Raul dell, False",
                     "18,Mariana Castillo, True", "176, Pdero Rodriguez, False"]))
