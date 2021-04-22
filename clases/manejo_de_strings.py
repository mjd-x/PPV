ingreso = input("Ingrese el valor: ")
# convertirlo en un int
valor = int(ingreso)
print(type(valor))

print("La informacion que ingreso el usuario es:{}".format(ingreso))
print(f"La informacion que ingreso el usuario es: {ingreso}")

multiplos = ingreso * 5
print(multiplos)

esta_incluido = "nico" in ingreso
print(esta_incluido)

print(chr(0x80F1))
ord('N')
len("Me dice la longitud de esta cadena")

print(type(str(False)))

cadena_extensa = "Esta es una cadena de caracteres mas extensa"
cadena_extensa[1]

print(cadena_extensa[1:10])
print(cadena_extensa[1:15:2])
print(cadena_extensa[:2:-1])  # splitting - al reves, corta primeros 2

cadena_extensa.upper()

print(cadena_extensa.split(' '))  # CSV
print(','.join(["Esta", "es", "la", "lista"]))
