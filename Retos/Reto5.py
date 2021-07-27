productos = {"1":	["Manzanas", 8000.0, 550],
             "2": [	"Limones",	2300.0,	15],
             "3": [	"Peras", 2500.0,	38],
             "4": [	"Arandanos",	9300.0,	55],
             "5": [	"Tomates"	, 2100.0,	42],
             "6": [	"Fresas"	, 4100.0,	33],
             "7": [	"Helado"	, 4500.0,	41],
             "8": [	"Galletas"	, 500.0	, 833],
             "9": [	"Chocolates",	3900.0,	999],
             "10": [	"Jamon",	17000.0	, 10]}


def imprimirResultado(productos):
    output = mayorMenor(productos)[:]+avgValor(productos)[:]
    print(output[0], output[1], round(output[2], 1), round(output[3], 1))


def ordenar(e):
    return e[1], e[0]


def mayorMenor(productos):
    valores = list(productos.values())
    valores.sort(reverse=True, key=ordenar)
    return [valores[0][0], valores[-1][0]]


def avgValor(productos):
    valorInventario = 0
    avg = 0
    for codigo in productos:
        valorInventario += productos[codigo][2]*productos[codigo][1]
        avg += productos[codigo][1]
    avg /= len(productos)
    return [avg, valorInventario]


def valores():
    codigo, nombre, precio, inventario = input().split()
    precio = float(precio)
    inventario = int(inventario)
    return [codigo, nombre, precio, inventario]


def actualizar(productos):
    producto = valores()
    if(not producto[0] in productos):
        print("ERROR")
        return
    productos[producto[0]] = producto[1:len(producto)]
    imprimirResultado(productos)


def borrar(productos):
    codigo, nombre, precio, inventario = valores()
    if(not (codigo in productos)):
        print("ERROR")
        return
    del(productos[codigo])
    imprimirResultado(productos)


def insertar(productos):
    producto = valores()
    if(producto[0] in productos):
        print("ERROR")
        return
    productos[producto[0]] = producto[1:len(producto)]
    imprimirResultado(productos)


switch_operaciones = {
    "AGREGAR": insertar,
    "ACTUALIZAR": actualizar,
    "BORRAR": borrar
}

operacion = input()

switch_operaciones[operacion](productos)
