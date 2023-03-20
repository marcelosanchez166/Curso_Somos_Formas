#programa para retornos multiples y multiples valores de retorno

#Retornos multiples

def dias_mes(mes):
    if mes==12 or mes==10 or mes==8 or mes ==7 or mes==5 or mes==3 or mes==1:
        return "El mes es de 31 dias"
    elif mes==6 or mes==9 or mes==11 or mes ==9 or mes==4:
        return "El mes es de 30 dias"
    elif mes==2:
        return "El mes es de 28 dias"
    else:
        return "No existe el mes"

print(dias_mes(16))
    

#Multiples valores de retorno

def aritme(a,b):
    return a+b, a-b, a*b, a/b

res=aritme(10, 5)
print(res) # La funcion return cuando tienen valores multiples los devuleve mediante tublas
print(f"El resultado de la funcion aritme es: {res[0]} {res[1]} {res[2]} {res[3]} ")#DE esta forma podemos acceder a la posicion de cada valor e imprimirlo por separado