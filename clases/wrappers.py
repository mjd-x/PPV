def suma(num1, num2):
    """ Se espera recibir un int """
    return num1 + num2


def wrapper_suma(a, b):
    """ No agrega ni modifica funcionalidad """
    return suma(int(a), int(b))

### Si se desea agregar un loggin por ejemplo antes de la suma?
