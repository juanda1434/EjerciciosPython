
def fibonacciRecursivo(a,b,cantidad):
    print(a)
    if cantidad>1:        
        fibonacciRecursivo(b,a+b,cantidad-1)


def fibonacciCiclo(cantidad):
    a=0
    b=1
    print(a)
    print(b)
    while(cantidad>2):
        c=a+b
        print(c)
        a=b
        b=c
        cantidad-=1

print("respuesta con recursividad")
fibonacciRecursivo(0,1,10)
print("Respuesta con while")
fibonacciCiclo(10)