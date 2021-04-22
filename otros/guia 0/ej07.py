def noDuplicados(texto):
    conjunto = set()
    lista = texto.split(' ')
    for elements in lista:
        conjunto.add(elements)
    return conjunto


texto = input('ingrese el texto: ').lower()
print(noDuplicados(texto))
