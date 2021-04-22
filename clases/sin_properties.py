class Factura:

    def __init__(self, numero, razon_social, productos):
        self.numero = numero
        self.razon_social = razon_social
        self.productos = productos


factura = Factura(133, "Sociedad SA", ['prod1', 'prod2'])

factura.numero = 454  # "Setter"
print(f"La razon social de la factura es:{factura.razon_social}")  # "Getter"

factura.numero = -456
factura.razon_social = {'Esto', 'Es', 'Un', 'Set'}
