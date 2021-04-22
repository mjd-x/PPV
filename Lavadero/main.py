import lavadero_ciudad_vehiculo
import ave_bandada

# 1. Hacer una bandada de dos gaviotas, una paloma, una cotorra y dos loros
# barranqueros, en forma de V.

gaviota1 = ave_bandada.Gaviota(2)  # 2 pescados
gaviota2 = ave_bandada.Gaviota(1)  # 1 pescado
paloma = ave_bandada.Paloma(10)
cotorra = ave_bandada.Ave()
loro1 = ave_bandada.Ave()
loro2 = ave_bandada.Ave()

bandada1 = ave_bandada.BandadaV()
bandada1.agregar_ave(gaviota1)
bandada1.agregar_ave(gaviota2)
bandada1.agregar_ave(paloma)
bandada1.agregar_ave(cotorra)
bandada1.agregar_ave(loro1)
bandada1.agregar_ave(loro2)

# 2. Representar a un auto que inicialmente esté limpio y ubicarlo en Buenos Aires.
BuenosAires = lavadero_ciudad_vehiculo.Ciudad()

auto = lavadero_ciudad_vehiculo.Vehiculo(0, 0)
BuenosAires.agregar_vehiculo(auto)

# 3. Crear a PyLav, un pequeño lavadero artesanal porteño donde trabajan 3 personas.
pyLav = lavadero_ciudad_vehiculo.LavArtesanal(4, 3)
BuenosAires.agregar_lavadero(pyLav)

# 4. Se necesita poder resolver los siguientes casos:
# a. Que esa bandada pase por encima del auto.
bandada1.ensuciar(auto)

# b. Que sobre Buenos Aires caiga una lluvia de ceniza volcánica.
BuenosAires.lluvia_ceniza(200)

# c. Que pase una paloma gorda por encima del mismo auto.
paloma2 = ave_bandada.Paloma(100)
paloma2.ensuciar(auto)

# d. Llevar el auto a PyLav, hacerlo lavar y saber cuánto costó.
pyLav.lavar(auto)

# e. Que la bandada se ponga en formación de W y vuelva a pasar por el auto
bandada1 = ave_bandada.BandadaW()
bandada1.agregar_ave(gaviota1)
bandada1.agregar_ave(gaviota2)
bandada1.agregar_ave(paloma)
bandada1.agregar_ave(cotorra)
bandada1.agregar_ave(loro1)
bandada1.agregar_ave(loro2)

# f. Llevarlo ahora al lavadero que cobre más barato de Buenos Aires
BuenosAires.mas_barato()
