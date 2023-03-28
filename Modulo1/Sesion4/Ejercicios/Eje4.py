# 4. Escribir una función que aplique un descuento a un precio y otra que aplique
# el IVA a un precio. Escribir una tercera función que reciba un diccionario con
# los precios y porcentajes de una cesta de la compra, y utilice las funciones
# para aplicar los descuentos y el IVA a los productos de la cesta y devolver el
# total a pagar final de la cesta.


def aplicar_descuento(precio,descuento):
    return precio * (1 - descuento / 100)

def aplicar_iva(precio,iva):
    return precio * (1 + iva / 100)


def calcular_total(cesta, descuento, iva):
    """
    Calcula el total a pagar por una cesta de la compra después de aplicar descuentos e IVA.

    Args:
        cesta (dict): Un diccionario con los nombres de los productos como claves y los precios como valores.
        descuento (float): El porcentaje de descuento a aplicar a los precios de la cesta.
        iva (float): El porcentaje de IVA a aplicar a los precios de la cesta después de aplicar el descuento.

    Returns:
        float: El total a pagar por la cesta después de aplicar descuentos e IVA.
    """
    total = 0
    for producto, precio in cesta.items():
        precio_descuento = aplicar_descuento(precio, descuento)
        precio_iva = aplicar_iva(precio_descuento, iva)
        total += precio_iva
    return total

cesta={"papas":1.24,"frijoles":0.5, "maiz":1.5,"Elotes":1.00,"Tomates":0.9}
print(calcular_total(cesta,0.10,0.13))




