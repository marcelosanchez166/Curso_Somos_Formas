#Progama para determinar la edad o para determinar si una persona es adulta
#Condiciones simples
#Condiciones anidadas

Edad=int(input("Ingrese su edad: "))
if Edad>=18:
    print("Eres mayor de edad ")
    if Edad>=60:
        print(" y eres una persona de la tercera edad")
    print("saliendo del programa.... ")
else:
    print("No eres mayor de edad")

#Condiciones multiples
if Edad >=1 and Edad<18:
    print("Eres menor de edad")
elif Edad >=18 and Edad<60:
    print("Eres adulto")
elif Edad>= 60 and Edad<=105:
    print("Eres una persona de la tercera edad")
else:
    print("Digite una edad valida")
