class Factura:

    def __init__(self, numero, razon_social, productos):
        self._numero = numero
        self.razon_social = razon_social
        self.productos = productos

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        if value <= 0:
            raise ValueError("El numero de la factura no puede ser negativo")

        self._numero = value


######
# NO TUVE QUE MODIFICAR EL CODIGO IMPLEMENTADO!!!
#######


factura = Factura(133, "Sociedad SA", ['prod1', 'prod2'])

factura.numero = 454  # "Setter"
print(f"La razon social de la factura es:{factura.razon_social}")  # "Getter"

factura.numero = -456
factura.razon_social = {'Esto', 'Es', 'Un', 'Set'}
