class Telefono:

    def __init__(self, procesador, pantalla, resolucion, bateria, precio):
        self._procesador = procesador
        self._pantalla = pantalla
        self._resolucion = resolucion
        self._bateria = bateria
        self._precio = precio

    def validar(self):
        validar = self._procesador >= 4 and self._pantalla > 5 and self._pantalla < 9 and self._resolucion >= 12 and self._bateria >= 18
        return validar


telefonos = []
cantidad = int(input())
while(cantidad > 0):
    procesador, pantalla, resolucion, bateria, precio = input().split()
    telefonos.append(Telefono(int(procesador), int(pantalla),
                     int(resolucion), int(bateria), int(precio)))
    cantidad -= 1
valor = -1
for tel in telefonos:
    if tel.validar():
        valor = 1
        print(tel._precio)

if valor < 0:
    print("NO DISPONIBLE")
