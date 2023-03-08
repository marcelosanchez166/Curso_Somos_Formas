# Ejercicio 7.
# Un supermercado ha puesto en oferta la venta al por mayor de cierto producto, ofreciendo 
# un descuento del 15% por la compra de más de 3 docenas y 10% en caso contrario. Además, 
# por la compra de más de 3 docenas se obsequia una unidad del producto por cada docena 
# en exceso sobre 3. Escriba un programa que determine el monto de la compra, el monto 
# del descuento, el monto a pagar y el número de unidades de obsequio por la compra de 
# cierta cantidad de docenas del producto


Docena=int(input("Cuantas docenas del producto desea llevar : "))
precio_Docena=12
OffDocena=0.15
Offnomarl=0.10
if Docena==3:
    subtotal=precio_Docena*Docena 
    descuento=subtotal*OffDocena
    total=subtotal-descuento
    print("Su total de la compra sin descuento: $",subtotal, "dolares,", "Descuento total: ", descuento,"dolares,", "Total a pagar es: $", total , "dolares")
elif Docena >3:
    unidades=Docena-3
    subtotal=precio_Docena*Docena 
    descuento=subtotal*OffDocena
    total=subtotal-descuento
    print("Su total de la compra sin descuento: $",subtotal, "dolares,", "Descuento total: ", descuento,"dolares,", "Total a pagar es:$", total,"dolares,",unidades,"Unidades gratis  por compras mayores a tres Docenas" )
else:
    subtotal=precio_Docena*Docena 
    descuento=subtotal*Offnomarl
    total=subtotal-descuento
    print("Su total de la compra sin descuento: $",subtotal, "dolares,", "Descuento total: ", descuento,"dolares,", "Total a pagar es:$", total, "dolares" )
