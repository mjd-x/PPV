def generar_dict():
    """Genera y retorna un diccionario ASCII, clave letra, valor numero"""

    dict = {chr(_): _ for _ in range(97, 123)}
    print(dict)


generar_dict()
