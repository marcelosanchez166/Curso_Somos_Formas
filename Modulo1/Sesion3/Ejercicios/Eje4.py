# 4. programa que solicite una fecha (día, mes, año) y una cantidad de días, elabore algoritmo para
# sumar días a la fecha capturada

# Pedir al usuario la fecha y la cantidad de días a sumar
dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))
dias_a_sumar = int(input("Ingrese la cantidad de días a sumar: "))
for i in range(dias_a_sumar):
    if mes==12 or mes==10 or mes==8 or mes ==7 or mes==5 or mes==3 or mes==1:
        days=dia+dias_a_sumar
        if days>31:
            mes=mes+1
            days=days-31
            if mes>12:
                anio+=1
                mes=1
        print(days,mes,anio)
    elif mes==6 or mes==9 or mes==11 or mes==9 or mes==4:
        days=dia+dias_a_sumar
        if days>30:
            mes=mes+1
            days=days-30
            # if mess>12:
            #     anio+=1
            #     mess=1
            # print(mess)
        print(days,mes,anio)
    elif mes==2:
        days=dia+dias_a_sumar
        if days>28:
            mes=mes+1
            days=days-28
        print(days,mes,anio)
    break
    # else:
    #     return "No existe el mes"
    # if dia 

# while True:


#Aqui pudiera sumar los dias al primer valor de la fecha que son los dias, luego haria un if para validar si el mes es de 28 30 o 31 dias, dependiendo lo que el usuario ingrese
#Luego si se llega al maximo de dias que puede tener el mes incrementar el mes y ademas incrementar los dias y si ya es diciembre incrementar el año