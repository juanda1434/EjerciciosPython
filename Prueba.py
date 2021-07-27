cantidadCalificar,recordadas = 6,4
notasIngresadas = "1 2 3 1 2 1 1 1".split()

ubicacionInicial=cantidadCalificar-recordadas
ubicacionInicial=(recordadas,ubicacionInicial)[ubicacionInicial-recordadas>=0]

recordadar={}
total=0
i=0
while i<ubicacionInicial:
    if i!=len(notasIngresadas) and notasIngresadas[i] in recordadar:
        ubicacionInicial+=1
        total+=1
    else:
        if i!=len(notasIngresadas):
            recordadas[notasIngresadas[i]]=0
    i+=1

print(total,recordadar)