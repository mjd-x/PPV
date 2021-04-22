class persona:
    def __init__(self, celulas, temperatura):
        self.celulas = celulas
        self.temperatura = temperatura
        self.enfermedades = []
    def enfermarse(self, enfermedad):
        self.enfermedades.append(enfermedad)
    def efectoDiario(self):
        #Produce los efectos de cada enfermedad que la persona tiene
        for i in range(0, len(self.enfermedades)):
            self.enfermedades[i].hacerEfecto(self)
    def estaSana(self):
        #Corrobora el estado de salud de la persona, evaluando si las enfermedades que tiene la persona
        #amenazan o no a las células, si las amenazan se mantienen en la persona y si no amenzan se eliminan
        i=0
        while i<len(self.enfermedades):
            if self.enfermedades[i].celulasAmenzadas<=0:
                self.enfermedades.pop(i)
            else:
                i=i+1
        # Finalmente corrobora si la persona tiene o no una enfermedad para determinar si esta sano o no
        if len(self.enfermedades)==0:
            return print("Esta sana")
        else:
            return print("No está sana")

class enfermedad:
    def __init__(self, celulasAmenazadas,tipo):
        self.celulasAmenzadas = celulasAmenazadas
        self.tipo=tipo
    def atenuar(self, mejora):
        self.celulasAmenzadas = self.celulasAmenzadas - mejora
    def agravar(self, gravedad):
        self.celulasAmenzadas = self.celulasAmenzadas + gravedad
    #cada enfermedad hará efectos sobre las celulas de la persona según el tipo de enfermedad que sea
    def hacerEfecto(self, persona):
        self.tipo.hacerEfecto(self,persona)

class infecciosa:
    def hacerEfecto(self, persona):
        persona.temperatura = persona.temperatura + (self.celulasAmenzadas / 1000)
    def duplicar(self):
        self.agravar(self.celulasAmenzadas * 2)

class autoinmune:
    def hacerEfecto(self, persona):
        persona.celulas = persona.celulas - self.celulasAmenzadas

class medicamento:
    #Un medicamento reduce las celulas amenzadas de todas las enfermedades que una persona tiene
    def curar(self, dosis, persona):
        for i in range(0, len(persona.enfermedades)):
            persona.enfermedades[i].atenuar(dosis * 15)

#IMPLEMENTACION
#Instanciación de enferemedades y personas
malaria = enfermedad(5000, infecciosa)
lupus = enfermedad(10000, autoinmune)
persona = persona(3000000, 36)
print(f"Celulas amenazadas por malaria: {malaria.celulasAmenzadas}, lupus {lupus.celulasAmenzadas}")
print(f"celulas de la persona: {persona.celulas}, temperatura {persona.temperatura}")
#Una persona se enferma con malaria y lupus
persona.enfermarse(malaria)
persona.enfermarse(lupus)
#Luego de un día con la enfermedad, la persona presenta la siguiente situacion
persona.efectoDiario()
print(f"celulas de la persona: {persona.celulas}, temperatura {persona.temperatura}")
#Las enfermedades se atenuan arbitrariamente segun los valores consignados
persona.enfermedades[0].atenuar(5000)
persona.enfermedades[1].atenuar(500)
print(f"malaria: {persona.enfermedades[0].celulasAmenzadas}, lupus {persona.enfermedades[1].celulasAmenzadas}")
#Se consulta si la persona está sana
persona.estaSana()
#La persona consume un medicamento y se consulta el efecto en la enfermedad que tenga
medicamento.curar(medicamento,300,persona)
print(f"enfermedad: {persona.enfermedades[0].celulasAmenzadas}")

'''Teórico: - Si queremos modelar una enfermedad que sea tanto infecciosa como autoinmune. ¿Cómo lo solucionamos?
Podría implementarse a través de un Patron Decorator, el cual permitiría extender comportamientos en forma dinamica
Entonces se tendría una enfermedad base con un comportamiento comun (en este caso lo único que haría es permanecer
en la persona) y a apartir de alli agregarle un decorador a esa enferemedad (que sería el tipo de enfermedad) 
armando una especie de capas dentro de la enfermedad, con lo que se modificaría su comportamiento'''