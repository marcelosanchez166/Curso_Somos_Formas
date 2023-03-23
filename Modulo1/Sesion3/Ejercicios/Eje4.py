# 4. programa que solicite una fecha (día, mes, año) y una cantidad de días, elabore algoritmo para
# sumar días a la fecha capturada


# Pedir al usuario la fecha y la cantidad de días a sumar
dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))
dias_a_sumar = int(input("Ingrese la cantidad de días a sumar: "))

for i in range(dias_a_sumar):
    dias=0
    if mes==12 or mes==10 or mes==8 or mes ==7 or mes==5 or mes==3 or mes==1:
        days=dia+dias_a_sumar
        print(days)
        if days>31:
            dias=days-31
            mes+=1
        print(dias,mes,anio)
    break
    # elif mes==6 or mes==9 or mes==11 or mes ==9 or mes==4:
    #     return "El mes es de 30 dias"
    # elif mes==2:
    #     return "El mes es de 28 dias"
    # else:
    #     return "No existe el mes"
    # if dia 

# while True:


#Aqui pudiera sumar los dias al primer valor de la fecha que son los dias, luego haria un if para validar si el mes es de 28 30 o 31 dias, dependiendo lo que el usuario ingrese
#Luego si se llega al maximo de dias que puede tener el mes incrementar el mes y ademas incrementar los dias y si ya es diciembre incrementar el año