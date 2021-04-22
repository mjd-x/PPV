"""Se ingresa una fecha e imprime los mes, dia, año por separado"""

fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")
fecha = fecha.split("/")

print(f"El dia ingresado fue: {fecha[0]}")
print(f"El mes ingresado fue: {fecha[1]}")
print(f"El año ingresado fue: {fecha[2]}")
