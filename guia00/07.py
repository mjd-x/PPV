def elimina_duplicado():
    """recibe texto y devuelve palabras en minuscula y sin duplicados en una coleccion"""

    cadena = str(input("Ingrese un texto: "))
    cadena = cadena.lower()
    palabras = set(cadena.split(" "))

    print(palabras)


elimina_duplicado()