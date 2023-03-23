# 2. Calcular la potencia de un número usando estructuras repetitivas, considere negativos y potencia 0

base=int(input("ingrese el numero base: "))
expo=int(input("Ingrese el exponente: "))

if expo == 0:
    print("Todo numero elevado al exponente cero es : 1") 
elif expo < 0:
    base = 1 / base
    expo = -expo
resultado = 1
for i in range(expo):
    resultado *= base
print(resultado) 
