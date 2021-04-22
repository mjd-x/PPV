def factorial():
    """Recibe como parametro un numero y devuelve su factorial. Implementación iterativa"""

    num = int(input("Ingrese el número: "))
    result = 1

    if num == 0:
        print(result)

    else:
        for _ in range(num):
            result *= _ + 1

        print(result)


def factorial_recursiva(num):
    """Recibe como parametro un numero y devuelve su factorial. Implementación recursiva"""

    if num == 1 or num == 0:
        return 1

    else:
        return num * factorial_recursiva(num - 1)


factorial()

inp = int(input("Ingrese el número: "))
print(factorial_recursiva(inp))
