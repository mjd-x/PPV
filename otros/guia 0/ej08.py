def ej08a(texto):
    """Arma una lista de bytes acorde al texto recibido por parametro"""
    indice = 0
    resultado = []
    current_byte = ""
    for i in texto:
        current_byte += i  # se agrega el nuevo caracter al byte actual
        indice += 1  # se incrementa en uno el indice
        if indice % 8 == 0:
            # Comienza un nuevo byte
            resultado.append(str(current_byte))
            current_byte = ""
    return resultado


print(ej08a("1001010101000101010101100101001010101010"))
