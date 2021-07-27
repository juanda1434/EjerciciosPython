class ExtraerDigito:

    def __init__(self,numero):
        self.numero=numero

    def extraer(self):
        numeroEnLetras = str(self.numero)
        mitad = len(numeroEnLetras)//2
        self.numeroEnLaMitad = numeroEnLetras[mitad]

    def mostrar(self):
        print("El numero en medio de",numero,"es igual a ",self.numeroEnLaMitad)



numero = int(input("Ingrese un numero "))

extractor = ExtraerDigito(numero)
extractor.extraer()
extractor.mostrar()


del(numero)
del(extractor)