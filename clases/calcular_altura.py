def calcular_altura(area, base):
    try:
        return area / base
    except ZeroDivisionError:
        return "No se puede dividir por cero\n"

flag = True

while flag:
    try:
        area = int(input("Ingrese el área: "))
        base = int(input("Ingrese la base: "))

        print(calcular_altura(area,base))
    except ValueError:  # mala conversion del dato
        opcion = str(input("Algo salió mal."))
