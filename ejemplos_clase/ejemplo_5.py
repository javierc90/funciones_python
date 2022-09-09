# Funciones [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

# Ejemplos de funciones integrador
import utils

# *****************************
#       PROFESOR LIVE CODE
# *****************************
# Debe copiar de los ejemplos anteriores
# cada unas de las funciones que se detallan



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    # *****************************
    #       PROFESOR LIVE CODE
    # *****************************
    # Deberá invocar cada una de las funciones
    # que se copiaron de ejemplos anteriores para
    # simular la compra de 4 productos

    # 1) Primero obtener la cantidad de productos comprados

    cantidad = utils.cantidad_productos()
    # 2) Obtener el precio de cada producto comprado
    # en una lista de "productos"
    precios_productos = utils.precio_productos_aleatorios(cantidad)

    # 3) Obtener el precio total de la compra
    precio_total = utils.calcular_precio_total(precios_productos)

    # 4) Imprimir en pantalla el precio total de la compra
    print(precio_total)

    print("terminamos")




