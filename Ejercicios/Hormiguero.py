class Hormiguero : 

    

    def __init__(self,cantidadHormigasInicial):
        self._cantidadHormigas=cantidadHormigasInicial


    def analizarPoblacion(self,meses):
        mesActual= 0
        muertesMensuales = 7000
        while mesActual<meses and self._cantidadHormigas>0:
            tasaCrecimiento = (0.4,0.315)[self._cantidadHormigas>28000]
            self._cantidadHormigas+=self._cantidadHormigas*tasaCrecimiento
            self._cantidadHormigas= (0,self._cantidadHormigas-muertesMensuales)[self._cantidadHormigas-muertesMensuales>0]
            self._imprimirDatos(mesActual)

            mesActual+=1            
    
    def _imprimirDatos(self,mesActual):
        print("\nPasado el mes",(mesActual+1),"\nCantidad Hormigas:",self._cantidadHormigas)