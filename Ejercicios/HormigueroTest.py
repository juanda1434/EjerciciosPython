from Hormiguero import Hormiguero

cantidadInicial = int(input("Ingresa la cantidad Hormigas Inicial "))
cantidadMeses = int(input("Ingresa cantidad de meses "))
hormiguero = Hormiguero(cantidadInicial)

print("Cantidad de meses es = a ",hormiguero._cantidadHormigas)
hormiguero.analizarPoblacion(cantidadMeses)