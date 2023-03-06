#programa para uso de sets
clientes={"Ernesto","Luisa","Diana", "Julia"}
print("Longitud del set: ", len(clientes))
#Son desordenados
print(clientes)#Por cada vez que se imprime los valores cambian de posicion
# No son indexados, No se pueden acceder a los indices de un set
#clientes[0]

#Sus elementos son inmutables
#clientes[2]="eva"

#Los sets son dinamicos pero no aceptan valores repetidos, por lo que si un elemento se agrega mas de una vez el set solo lo guardara una vez
clientes.add("eva")
clientes.add("eva")
print(clientes)

#Se pueden eliminar 
clientes.discard("Ernesto")
print(clientes)


for i in clientes:
    print("clientes: ",i)

"""Frozenset son estaticos no se pueden modificar ni eliminar"""
lista1=frozenset({3,16,8})
print(lista1)