#PAso de parametros valor/referencia

#PAso por copia inmutable

#En esta funcion el valor de X se mantiene ya que es un valor dado por el usuario lo cual lo hace inmutable
x=2
def modificar_variable(x):
    x=+10
    return x

z=modificar_variable(x)
print(z)
print(x)



#Paso por direccion (Mutables), Esta funcion al usar una lista y por ser mutable la lista V agrego el valor que se agrego dentro de la funcion
v=[3,1,4,5]

def modificar_vector(w):
    w.append(2)
    return w

s=modificar_vector(v)
print(s)
print(v)

