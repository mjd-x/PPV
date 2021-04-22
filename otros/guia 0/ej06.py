def palabras():
    lista = []
    palabra = input('ingrese palabra: ')
    while palabra != 'exit':
        lista.append(palabra)
        palabra = input('ingrese palabra: ')
    lista.sort()
    return lista


print(palabras())
