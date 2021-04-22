print('***ingrese parametros de inicio y fin***')
a = int(input('parametro de inicio'))
b = int(input('parametro de fin'))
print('los valores insertados son {} y {}, y el resultado:'.format(a, b))
z = []
for i in range(a, b):
    if (i % 7) == 0 and (i % 5) != 0:
        print(i)
        z.append(i)
print(*z, sep=',')
