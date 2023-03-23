# Ejercicio 9.
# El promedio de prácticas de un curso se calcula en base a cuatro prácticas calificadas de las
# cuales se elimina la nota menor y se promedian las tres notas más altas. Escriba un
# programa que determine la nota eliminada y el promedio de prácticas de un estudiante.


prac1 = int(input("Digite la nota practica 1 : "))
prac2 = int(input("Digite la nota practica 2 : "))
prac3 = int(input("Digite la nota practica 3 : "))
prac4 = int(input("Digite la nota practica 4 : "))

if prac2>prac1 and prac3>prac1 and prac4>prac1:
    print("La nota de la practica con menor nota es ",prac1, "El promedio es: ", (prac2+prac3+prac4)/4)
elif prac1>prac2 and prac3>prac2 and prac4>prac2:
    print("La nota de la practica con menor nota es ",prac2, "El promedio es: ", (prac3+prac4+prac1)/4)
elif prac1> prac3 and prac2> prac3 and prac4> prac3 :
    print("La nota de la practica con menor nota es ",prac3, "El promedio es: ", (prac4+prac1+prac2)/4)
elif prac1> prac4 and prac2> prac4 and prac3> prac4 :
    print("La nota de la practica con menor nota es ",prac4, "El promedio es: ", (prac1+prac2+prac3)/4)
