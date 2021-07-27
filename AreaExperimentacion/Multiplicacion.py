"""Multiplicacion  con sumas sucesivas input: 2 numeros enteros que van a ser multiplicados
 output: 1 numero entero equivalente a la multiplicacion de los 2 numeros"""

numeroUno = int(input("Ingresa el primer numero "))
numeroDos = int(input("Ingresa el segundo numero "))
multiplicacion=0
for i in range(0,numeroDos):
    multiplicacion+=numeroUno

print (numeroUno,"*",numeroDos,"=",multiplicacion)

"""El for funciona como ciclo que repite una operacion: para este caso repite multiplicacion+=numeroUno

cuantas veces va a repetir ? 

la cantidad de veses que se defina en la funcion range(unNumero,otroNumero)
para este ejemplo el range esta entre 0 a lo que esta almacenado en la variable numeroDos 

si queremos multiplicar 4 * 5 el rango estaria entre 0 a 5 esto significa que el for o el ciclo
se va a repetir 5 veces

"""
