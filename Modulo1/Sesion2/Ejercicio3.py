# Ejercicio 3.
# Elaborar un programa que permita realizar una conversión de monedas, sea esta de dólar a colon o
# viceversa, considere al menos 3 conversiones (Bitcoin) diferentes y permita al usuario seleccionar
# que conversión desea hacer mediante un menú.

print("Ingrese la opcion de conversion que desee")
print("1- dolar a Colon")
print("2- Colon a Dolar")
print("3- dolar a Bitcoin")
print("4- Bitcoin a Dolar")
# print("5- Bitcoin a colon")
# print("6- Colon a Bitcoin")
opcion=int(input("Ingrese una opcion para conversion de moneda: "))

colonadolar=0.11
dolaracolon=9
BTCadolar=23249
DolaraBTC=0.00004334445841099215
BTCacolon=202.284,51
ColonaBTC=0.000004951314286

if opcion==1:
    dolar=int(input("Ingrese la cantidad de dolares a convertir a  colones: "))
    print("La conversion de dolares a colon es: ", dolar*dolaracolon, "colones")
elif opcion==2:
    colon=int(input("Ingrese la cantidad de colones a convertir a  dolares: "))
    print("La conversion de colones a Dolares es: ", colon*colonadolar, "dolares")
elif opcion==3:
    dolar=int(input("Ingrese la cantidad de Dolar a convertir a Bitcoin: "))
    print("La conversion de Dolares a BTC es: ", dolar*DolaraBTC)
elif opcion==4:
    Bitcoin=float(input("Ingrese la cantidad de Bitcoin a convertir a dolares: "))
    print("La conversion de BTC a Dolares es: ", Bitcoin*BTCadolar)
# elif opcion==5:
#     colon=float(input("Ingrese la cantidad de Colon a convertir a Bitcoin: "))
#     print("La conversion de Colon a BTC es: ", colon*ColonaBTC, "Bitcoins")
# elif opcion==6:
#     BTC=int(input("Ingrese la cantidad de Bitcoin a convertir a Colon: "))
#     print("La conversion de BTC a Colones es: ", BTC*BTCacolon, "Colones")
else:
    print("La opcion ingresada no corresponde a nada")