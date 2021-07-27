def totalIguales(notasIngresadas):
    notasRepetidasTotal ={}
    total=0
    for i in range(0,len(notasIngresadas)):
        if notasIngresadas[i] in notasRepetidasTotal:
            total+=1
        else:
            notasRepetidasTotal[notasIngresadas[i]]=0
    return total
cantidadCalificar, recordadas = input().split()
cantidadCalificar,recordadas=int(cantidadCalificar),int(recordadas)
notasIngresadas = input().split()
guardar = []
cantidad = {}
i = 0
limite = cantidadCalificar-1
final = cantidadCalificar-recordadas
for nota in notasIngresadas:
    if len(guardar) == recordadas and (i) < len(notasIngresadas) and (i) <= cantidadCalificar and not notasIngresadas[i] in guardar and i != final:
        del(cantidad[guardar[0]])
        del(guardar[0])
    if not nota in guardar and i != final:
        guardar.append(nota)
        cantidad[nota] = 0
    elif nota in guardar:
        cantidad[nota] += 1
        if len(guardar) < recordadas:
            limite += 1
    if limite == i:
        break
    i += 1
totalProfesor = 0
for sumar in cantidad:
    totalProfesor += cantidad[sumar]
print(totalIguales(notasIngresadas),totalProfesor)