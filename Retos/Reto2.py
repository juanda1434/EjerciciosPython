distancia, velocidadPromedio, tiempo = input().split()
distancia, velocidadPromedio, tiempo = float(
    distancia), float(velocidadPromedio), float(tiempo)
if distancia > 0 and velocidadPromedio > 0 and tiempo > 0:
    velocidad = (distancia/1000)/(tiempo/3600)
    if velocidad > velocidadPromedio:
        paraRecord = velocidadPromedio + velocidadPromedio*0.25
        if velocidad > paraRecord:
            print("ENTREVISTA")
        else:
            print("NUEVO RECORD")
    else:
        print("NORMAL")
else:
    print("VALOR ERRADO")
