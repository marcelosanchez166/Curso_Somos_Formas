# Ejercicio 10.
# En un estacionamiento cobran $1.50 por hora o fracción. Escriba un programa que 
# determine cuanto debe pagar un cliente por el estacionamiento de su vehículo, conociendo 
# el tiempo de estacionamiento en horas y minutos 

print(" Ejemplo: \n"
    "si solo estuvo 1 hora exacta solo colocar 1\n" 
    "si estuvo mas de una hora colocar por ejemplo: 1.03 ó 2.25\n")


Hparking=int(input("Ingrese cuantas horas estuvo estacionado: "))
Mparking=int(input("Ingrese los minutos que se estuvo: "))
precio=1.50
horas=0


if Hparking==1 and Mparking==0:
    horas=horas+1
    pago=horas*1.50
    print(pago)
elif Hparking>=1 and Mparking>0:
    horas=horas+1+Hparking
    print("H: ",horas)
    pago=horas*1.50
    print(pago)
elif  Hparking<=0 and Mparking>0:
    horas=horas+1
    pago=horas*1.50
    print(pago)
else:
    print("Estuvo menos de una hora y menos de un minuto")