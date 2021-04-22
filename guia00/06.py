def ordena():
    """recibe una serie de palabras y las muestra ordenadas alfabeticamente y capitalizadas, hasta que se ingrese 'exit'"""
    palabra = str(input("Ingrese palabra: "))
    lista = [palabra]

    while palabra != "exit":
        palabra = str(input("Ingrese palabra: "))
        lista.append(palabra)

    lista.pop()
    lista.sort()
    largo = len(lista)

    for i in range(largo):
        print(i)
        lista[i] = lista[i].title()

    print(lista)


ordena()
