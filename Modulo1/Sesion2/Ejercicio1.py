#Ejercicios
# Ejercicio 1.
# Programa que solicite el año por teclado y me diga si es bisiesto o no.
# Enunciado año bisiesto:
# Año bisiesto es el divisible entre 4, salvo que sea año secular -último de cada siglo,
# terminado en «00»-, en cuyo caso también ha de ser divisible entre 400
# Si el a;o es divisible entre 4 y no entre 100 es bisiesto
# Si el a;o es divisible entre 100 y entre 400 es bisiesto

year=int(input("Ingrese el a?o: "))
if year%4==0 and year%100!=0:
    print("el a?o  es Bisiesto")
elif year%100==0 and year%400==0:
    print("El a?o es bisiesto")
else:
    print("El a?o es secular")
