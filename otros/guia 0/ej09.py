def ej09(texto):
    digito = 0
    letra = 0
    simbolo = 0
    for leter in texto:
        if leter.isdigit() == True:
            digito += 1
        elif leter.isalpha() == True:
            letra += 1
        else:
            simbolo += 1
    resultado = (letra, digito, simbolo)
    return resultado


print(ej09("Esta es una manana lluviosa!! 25 dias mas seran asi??"))
