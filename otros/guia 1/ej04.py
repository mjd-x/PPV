def desglosar(fecha):
    fecha = fecha.split('/')
    print('el dia ingresado fue: {}'.format(fecha[0]))
    print('el mes ingresado fue: {}'.format(fecha[1]))
    print('el año ingresado fue: {}'.format(fecha[2]))


desglosar('6/12/1986')
