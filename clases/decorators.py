def log_audit(func):
    """ Recibe como parametro una funcion x"""

    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"El resultado de la funcion es: {resultado}")
        return resultado

    return wrapper  # Python permite retornar una funcion porque es un objeto!


@log_audit
def suma(num1, num2):
    """ Se espera recibir un int """
    return num1 + num2


num1 = 45
num2 = 56

# Ejecuto el metodo sin haberlo modificado
suma(num1, num2)
