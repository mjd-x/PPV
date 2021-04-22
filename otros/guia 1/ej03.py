def crear_mes():
    nombre = input('Ingrese el nombre del mes: ')
    abreviatura = input('Ingrese el abrevitura: ')
    dias = int(input('Ingrese la cantidad de dias: '))
    return "Se creo el mes {}, que se abrevia {} y contiene {} dias".format(
        nombre, abreviatura, dias)


print(crear_mes())
