#productos = [{'codigo': 1233, 'desc': 'Arroz Integral 1 kilo', 'precio': 66.33},
#             {'codigo': 55, 'desc': 'Agua mineral 1 litro', 'precio': 75.12}
#             ]


class Producto:
    catal = []

    def __init__(self, cod, des, prec):
        prod = {'codigo': int(cod), 'desc': str(des), 'precio': float(prec)}
        self.catal.append(prod)


def buscar(id):  # b
    """Busca un producto y devulve esa entrada en el dict"""

    for _ in range(len(productos)):
        if id == productos[_]['codigo']:
            # print(f"Código: {productos[_]['codigo']}, "
            #      f"Descripción: {productos[_]['desc']}, "
            #      f"Precio: {productos[_]['precio']}")
            return productos[_]

    else:
        print("No se encontró el producto")
        return False


# i = int(input("numero: "))
# buscar(i)


def factura():  # d
    """Recibe codigo y cantidad, y muestra y genera factura con su total y los productos"""
    total = 0.00
    fact = []
    id = (input("Ingrese el código de producto a agregar: "))

    while not id == "F":
        if buscar(int(id)) is not False:
            produc = buscar(int(id))
            cant = int(input("Ingrese la cantidad: "))

            agrega = [cant, int(id), produc['desc'], produc['precio']]
            fact.append(agrega)
            total += cant * produc['precio']

            id = input("Ingrese el código de producto a agregar: ")

        else:
            id = input("Ingrese el código de producto a agregar: ")

    if not fact:
        print("No agregaste ningún producto")

    else:
        print(f"Factura: {fact}\n    Total: {total}")


# factura()


def agregar():
    codigo = int(input("Ingrese el código: "))
    descrip = input("Ingrese la descripción: ")
    precio = float(input("Ingrese el precio: "))

    prod = Producto(codigo, descrip, precio)

    print(prod.catal)

agregar()