
class Persona:
    #Definir atributos privados aplicando el concepto de encapsulamiento
    #el _ antes del nombre del atributo define el atributo como no accesible directamente fuera de la clase
    #cada uno de estos se les puede llamar tambien variables de la clase o variables de cada objeto o instancia
    _nombre = "objeto sin nombre"
    _edad   = "objeto sin edad"

    #metodo para construir objetos o instancias de la clase; _init_(self,valores ingresados)
    #entre los parentesis van los parametros o variables que se envian como valores de entrada
    #self es un parametro que se pasa junto a los valores de entrada para acceder a los atributos de la clase
    def __init__(self,nombreIngresado,edadIngresada):
        self.nombre=nombreIngresado
        self.edad=edadIngresada

    #funcion de la clase que podra ser utilizada por los objetos que se creen para imprimir nombre y edad
    #se le debe colocar un nombre a la funcion o metodo para este caso (imprimirInformacion) 
    #entre parentesis () solo recibe self para acceder a los atributos propios de la clase.
    #utiliza la funcion propia de python llamada print() para imprimir en la consola 
    def imprimirInformacion(self):
        print("Nombre : ",self.nombre,"edad : ",self.edad)
       

#instanciaDeUnaPersona es una variable que va almacenar un objeto nuevo de la clase Persona
#el _init_(self,valores ingresados) se convierte en Persona(valores ingresados)
#Creando una instancia de persona llamada juan con 24 años
#se envia como parametros de entrada Juan y 24
#recuerda el orden (self,nombreIngresado,edadIngresada)
# self no se ingresa pero nombre y edad si en su orden respectivo ("Juan",24)
# imaginese que python lo interpreta asi  (nombreIngresado="Juan",edadIngresada=24)
#instanciaDeUnaPersona= Persona("Juan",24)

#para ejecutar la funcion nombreVariable.nombreFuncion()
#instanciaDeUnaPersona.imprimirInformacion()