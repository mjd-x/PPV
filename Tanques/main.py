import tanques

# M4 tiene 51mm de blindaje y soporta hasta 400 puntos de daño.
sherman = tanques.Tanque(51, 400)  # blindaje, daño

# PzV tiene 85 mm de blindaje y soporta hasta 500 puntos de daño
panther = tanques.Tanque(85, 500)

# proyectiles perforantes (AP) que son capaces de penetrar un blindaje de 92mm y que provocan 110 puntos de daño
ap_sherman = tanques.Proyectil(92, 110)
sherman.agregar_proyectil(ap_sherman)

#  obuses (HE) que penetran hasta 38mm de blindaje y realizan 250 puntos de daño.
obus_sherman = tanques.Proyectil(38, 250)
sherman.agregar_proyectil(obus_sherman)

# proyectiles perforantes que son capaces de penetrar un blindaje de 135mm y que provocan 175 puntos de daño
ap_panther = tanques.Proyectil(135, 175)
panther.agregar_proyectil(ap_panther)

# obuses que penetran hasta 53mm de blindaje y realizan 350 puntos de daño
obus_panther = tanques.Proyectil(53, 350)
panther.agregar_proyectil(obus_sherman)

sherman.dispara(panther)
