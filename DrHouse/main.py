import enfermedad_persona

# Tomar una malaria que afecta 5000 células amenazadas

malaria = enfermedad_persona.EnfermedadInfecciosa(5000)

# un lupus de 10000

lupus = enfermedad_persona.EnfermedadAutoinmune(10000)

# persona con 36 de temperatura y con 3.000.000 de células

pepe = enfermedad_persona.Persona(36, 3000000)
pepe.ver_estado()

# 1. Hacer que una persona contraiga malaria y lupus, y que dicha persona viva un día
# de su vida para que las enfermedades hagan su efecto.

pepe.contraer(malaria)
pepe.contraer(lupus)

pepe.dia_siguiente()
pepe.ver_estado()

# 2. Hacer que dicha malaria se atenúe en 5000 y el lupus en 500 y preguntar si la
# persona está sana.

malaria.atenuar(5000)
lupus.atenuar(500)
pepe.ver_estado()

# 3. Hacer que la persona reciba una dosis de 300 ml de medicamento.

pepe.tomar_medicacion(300)
pepe.ver_estado()
