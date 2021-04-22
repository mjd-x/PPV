def factorial(x):
    if x == 0:
        return 1
    elif x != 1:
        x = x * factorial(x-1)
    return x


def facIterativo(x):
    resultado = 1
    if x == 0:
        return 1
    while x >= 1:
        resultado = resultado * x
        x -= 1
    return resultado


n = int((input('Calcular el factorial de: ')))
print('el factorial de {} por recursividad es: {} igual que iterativo es: {}'.format(
    n, factorial(n), facIterativo(n)))
