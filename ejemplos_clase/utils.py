import random


def imprimir_nombre(nombre, apellido):
    nombre_completo = nombre + ' ' + apellido
    print(nombre_completo)


def cantidad_productos():
    productos_comprados = int(input("¿Cuántos productos compró?: "))
    return productos_comprados

def precio_productos(cantidad_productos):
    productos = []  # lista donde almacenaremos los precios, comienza vacia

    # Realizar un bucle que se ejecute una vez
    # por cada producto comprado, 
    # que permita ingresar el precio por consola
    for i in range(cantidad_productos):
        print("Indique precio del producto", i)
        precio = int(input())
        productos.append(precio)

    # Retornar la lista de precios de productos
    return productos

def precio_productos_aleatorios(cantidad, valor_min = 1, valor_max = 1000 ):
    productos = []  # lista donde almacenaremos los precios, comienza vacia
    
    # Realizar un bucle que genere números aleatorios
    # comprendidos entre el rango especificado
    for i in range(cantidad):        
        precio = random.randint(valor_min, valor_max)
        print("Precio aleatorio del producto", i + 1 , "es", precio)
        productos.append(precio)

    # Retornar la lista de precios de productos
    return productos

def calcular_precio_total(lista_productos):
    precio_total = sum(lista_productos)
    return precio_total


def calcular_precio_total_bucle(lista_productos):
    precio_total = 0
    # Profesor: Implementar un bucle que
    # recorra la variable "lista_productos"
    # y obtener el precio total de la lista

    precio_total = 0
    for precio in lista_productos:
        precio_total += precio
    return precio_total

print(__name__)