import random

class Tanque:
    """un tanque puede llevar cualquier cantidad de proyectiles de cualquier tipo
       para disparar elige al azar un proyectil"""

    def __init__(self, blindaje, dano):
        self.blindaje = blindaje
        self.dano = dano
        self.proyectiles = []

    def get_blindaje(self):
        return self.blindaje

    def get_dano(self):
        return self.dano

    def set_dano(self, dano):
        self.dano = dano

    def agregar_proyectil(self, proyectil):
        self.proyectiles.append(proyectil)

    def dispara(self, tanque):
        """dispara proyectil random que lleve el tanque si el otro tanque no fue destruido"""

        if(tanque.get_dano()) <= 0:
            print("El tanque está destruido.")

        else:
            rand = random.randint(0, len(self.proyectiles) - 1)
            proy = self.proyectiles.pop(rand)

            if proy.blindaje > tanque.get_blindaje():
                tanque.set_dano(tanque.get_dano() - proy.dano)
                print(f"Se disparó el proyectil, que causó {proy.dano} de daño.")

                if tanque.get_dano() <= 0:
                    print("El tanque fue destruido.")

                else:
                    print(f"Al tanque le quedan {tanque.get_dano()} puntos de daño.")

            else:
                print("Se disparó el proyectil, pero no pudo penetrar el blindaje del tanque.")
                print(f"Proyectil: {proy.blindaje}mm, Tanque: {tanque.get_blindaje()}mm.")


class Proyectil:
    def __init__(self, blindaje, dano):
        self.blindaje = blindaje
        self.dano = dano