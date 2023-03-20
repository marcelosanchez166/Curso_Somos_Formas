# Ejercicio 8.
# Una compañía dedicada al alquiler de automóviles cobra un monto fijo de $30.00 para los 
# primeros 300 km de recorrido. Para más de 300 km y hasta 1000 km, cobra un monto 
# adicional de $ 0.25 por cada kilómetro en exceso sobre 300. Para más de 1000 km cobra un 
# monto adicional de $ 0.50 por cada kilómetro en exceso sobre 1000. Los precios ya incluyen 
# el 13% del impuesto general a las ventas, IVA. Escriba un programa que determine el monto 
# a pagar por el alquiler de un vehículo y el monto incluido del impuesto

MontoFijo=30.0
montoAdicional1=0.25
montoAdicional2=0.50
iva=0.13
kilometrosRecorridos=int(input("Ingrese la cantidad de Kilometros recorridos: "))

if kilometrosRecorridos<=300:
    print("El monto fijo a pagar es: ", MontoFijo, "con el", iva," % de iva incluido, Su total a pagar es: ", MontoFijo)
elif kilometrosRecorridos>300 and kilometrosRecorridos<=1000:
    totalkm=kilometrosRecorridos-300
    print("El monto fijo a pagar es: ", MontoFijo, "con el", iva," % de iva incluido","Mas el costo adicional por kilometro extra es de"
        ,montoAdicional1," Su total a pagar es: ",MontoFijo+(totalkm*montoAdicional1) )
elif kilometrosRecorridos>1000:
    totalkm=kilometrosRecorridos-300
    print("El monto fijo a pagar es: ", MontoFijo, "con el", iva," % de iva incluido","Mas el costo adicional por kilometro extra es de"
        ,montoAdicional2," Su total a pagar es: ",MontoFijo+(totalkm*montoAdicional2) )


