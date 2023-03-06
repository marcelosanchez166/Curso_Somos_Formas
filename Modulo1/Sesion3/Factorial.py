#programa para calcular el factorial de un numero

numero=int(input("Ingrese un numero "))
for i in range(1,numero):
    numero = numero*i
print(numero)