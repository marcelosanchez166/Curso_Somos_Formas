# 7. Crear un programa que solicite N números por teclado y los guarde en una lista, a partir de la lista,
# ordenarlos de menor a mayor (no se vale usar sort), mostrar el mayor, el menor, y la sumatoria y
# promedio de todos

lista=[]
count=0
N_Numbers=int(input("Cuantos numeros desea ingresar: "))
for i in range(N_Numbers):
    Number=int(input("Ingrese un numero: "))
    lista.append(Number)
    count=count+lista[i]


for i in range(len(lista)):
    for j in range(len(lista)):
        if lista[i]< lista[j]:
            temp=lista[i]
            lista[i]=lista[j]
            lista[j]=temp
# suma=lista[i]+lista[j]
print("Lista ordenada de menor a mayor: ",lista,"La suma de todos los numeros ingresados es: ",count, "El menor valor de la lista es: ",lista[0],
    "El numero mayor de la lista es :",lista[-1], "El promedio de todos los numeros es: ",count/len(lista))
# print(f"El número mayor es: {lista[-1]}")

