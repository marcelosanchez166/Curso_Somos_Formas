# Ejercicio 5.
# Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas
# h, que indique qué hora marcará el reloj dentro de h horas


T=int(input("Ingrese la hora actual: "))
H=int(input("Ingrese la cantidad de horas: "))
horas=(T+H)%12
print("En ", H,"Horas el reloj marcara las ", horas )
