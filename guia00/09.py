def cuenta(cadena):
    """recibe por parámetro un texto y devuelve una tupla
    La tupla tiene la cantidad de letras, la cantidad de dígitos y otros símbolos."""

    letras = 0
    digitos = 0
    simbolos = 0

    for _ in cadena:
        if _.isalpha():
            letras += 1
        elif _.isdigit():
            digitos +=1
        elif not _.isalpha():
            simbolos += 1

    return (letras, digitos, simbolos)


cad = str(input("Ingrese el texto: "))
print(cuenta(cad))