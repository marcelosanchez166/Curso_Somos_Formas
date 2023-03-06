# Ejercicio 6.
# Calcular el sueldo semanal de una persona, solicitar nombre, DUI y horas trabajadas. La hora normal 
# se paga en $ 10.00 hasta 40 horas, si tiene mas de 40 horas se pagan como extras al 200%. Imprima 
# los datos de la persona y el sueldo a remunerar


Name=input("Ingrese su Nombre: ")
DUI=int(input("Ingrese su Dui, Sin guiones: "))
Htrabajadas=int(input("Numero de horas trabajadas: "))

Pago_Hora=10
pagoextra=Pago_Hora*2.0

#80dolares despues de las 40 horas
if Htrabajadas<=40:
    print("Estimado ",Name,"Con Dui", DUI, "Informar que Su salario por las ", Htrabajadas,"horas trabajadas es: ", 10*Htrabajadas)
elif Htrabajadas>40:
    HExtra=Htrabajadas-40
    print("Estimado ",Name,"Con Dui", DUI, "Informar que Su salario por las ", Htrabajadas,"horas trabajadas es: ", (40*Pago_Hora)+(HExtra*pagoextra) )
