from os import system
catalogo = [
    {'codigo': 1221, 'desc': "Leche entera 1 litro", 'precio': 54.34},
    {'codigo': 2231, 'desc': "Queso untable 200gs", 'precio': 145.34},
    {'codigo': 3213, 'desc': "Harina 0000 1 kilo", 'precio': 24.32},
    {'codigo': 3431, 'desc': "Detergente Biodeg.", 'precio': 80.14},
    {'codigo': 5431, 'desc': "Jabon cremoso 1 unidad", 'precio': 50.00},
    {'codigo': 1233, 'desc': "Arroz Integral 1 kilo", 'precio': 66.33},
    {'codigo': 1589, 'desc': "Gaseosa Cola 1 Litro", 'precio': 78.65},
    {'codigo': 985, 'desc': "Cerveza Rubia lata 476", 'precio': 54.00},
    {'codigo': 84, 'desc': "Manteca Pack 500gs", 'precio': 124.65},
    {'codigo': 155, 'desc': "Fideos Tallarin 1 kilo", 'precio': 35.23},
    {'codigo': 9857, 'desc': "Jamon Cocido 200 gs", 'precio': 99.32},
    {'codigo': 4756, 'desc': "Queso Dambo 200 gs", 'precio': 98.34},
    {'codigo': 5661, 'desc': "Patitas de Pollo 400 gs", 'precio': 144.99},
    {'codigo': 1763, 'desc': "Comida Gatos 500gs", 'precio': 86.25},
    {'codigo': 1356, 'desc': "Tostaditas Light 265 gs", 'precio': 32.50},
    {'codigo': 1524, 'desc': "Salchichas Super Pancho", 'precio': 95.20},
    {'codigo': 7341, 'desc': "Salsa de Tomate 500 gs", 'precio': 47.90}
]


def buscar(codigo):
    for producto in catalogo:
        if codigo == producto.get('codigo'):
            print("El producto {}, de codigo {} sale ${}".format(
                producto.get('desc'), producto.get('codigo'), producto.get('precio')))
            return None
    else:
        print('No se pudo encontrar el producto buscado')
        return None


def nuevaFactura():
    factura = list()
    codigo = input('Ingrese el codigo de producto: ').lower()
    while codigo != 'f':
        if codigo.isdigit() == True:
            codigo = int(codigo)
            for producto in catalogo:
                if codigo == producto.get('codigo'):
                    cant = int(input('Ingrese la cantidad: '))
                    fila = {'codigo': producto.get('codigo'), 'desc': producto.get(
                        'desc'), 'precio': producto.get('precio'), 'cant': cant}
                    factura.append(fila)
            else:
                print('Producto no encontrado')
                codigo = input(
                    'Ingrese el codigo de producto o f para terminar: ').lower()
        else:
            system("cls")
            print('Codigo no valido, ingrese un codigo valido o F para terminar')
            codigo = input('Ingrese el codigo de producto: ').lower()
    print('Carga de productos terminada, su factura es: ')
    total = 0
    system("cls")
    for fila in factura:
        total += (fila.get('precio')*(fila.get('cant')))
        print('{} de {} a {:.2f}'.format(fila.get('cant'), fila.get(
            'desc'), (fila.get('precio')*fila.get('cant'))))
    print('Total de la factura: {:.2f}'.format(total))


def cargarProducto():
    codigo = int(input('Ingrese el codigo del producto: '))
    descripcion = input('Ingrese la descripcion: ')
    precio = float(input('Ingrese el precio unitario: '))
    round(precio, 2)
    prod = {'codigo': codigo, 'desc': descripcion, 'precio': precio}
    catalogo.append(prod)
    print('Se agrego el producto {}'.format(prod))
