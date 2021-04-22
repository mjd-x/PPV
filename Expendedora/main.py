import maquina

# Preparar una bebida con la máquina, y que eso actualice las cantidades de susingredientes almacenados.
maq1 = maquina.Maquina(300, 200, 300, 400, 500, 600, 30, 800, 400)
beb1 = maquina.Bebida()
maq1.preparar_bebida(beb1)

# Preparar una bebida con la máquina que no tieneingredientes suficientes
beb2 = maquina.Bebida()
maq1.preparar_bebida(beb2)

# Consultar a la máquina si necesita reabastecimiento.
maq1.consultar_ingredientes()

# Consultar la recaudación
maq1.consultar_recaudacion()

# Consultar qué bebida fue más veces servida por la máquina
print("Bebida popular:")
print(maq1.bebida_popular())

# Averiguar cuántas máquinas deben reabastecerse
maq2 = maquina.Maquina(200, 200, 200, 200, 200, 200, 200, 200, 500)
mercado = maquina.Red()
mercado.agregar(maq1)
mercado.agregar(maq2)

maq2.preparar_bebida(beb1)

mercado.reabastecimiento()

# Calcular la recaudación total de todos las máquinas conectadas
mercado.calcular_recaudacion()

# Averiguar la bebida favorita del mercado
mercado.bebida_popular()