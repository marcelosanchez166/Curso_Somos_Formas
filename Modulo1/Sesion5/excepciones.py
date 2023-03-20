#Las excepciones se colocan en el orden de prioridad y por ultimo las excepciones generales

try:
    saludo="hola"
    #4/0
    #v=[5,4,5,6]
    #v[5]
    #saludo+10
    int(saludo)
    print("transaccion exitosa")
except ZeroDivisionError as e:
    print("problema en la division ")
except ValueError as e:
    print("error en el tipo de valor")
except IndexError as e:
    print("indice fuera de rango")
except TypeError as e:
    print("operacion no valida, No puede concatenar cadenas con int, float,boolean")
except Exception as e: #El Exception as e=siginifica que captura el error de la operacion y la imprime 
    print("Ocurrio un error ", e )

suma=4+1
print(suma)
