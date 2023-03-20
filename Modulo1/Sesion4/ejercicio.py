# Crear un programa que capture los datos de N empleados:

#  - nombre
#  - cargo
#  - sueldo

# Crear el siguiente menu
#     1. Agregar empleado
#     2. Imprimir lista
#     3. Salir

# para cada empleado construir un diccionario que se ira agregando a una lista que será impresa con la opción 2 del menu.

# Indicaciones de entrega: subir PDF con captura del codigo fuente.

print(" Menu para agregar empleados \n", "\n"
    "  1. Agregar empleado\n"
    "  2. Imprimir lista\n"
    "  3. Salir")

print("----------\n")

# dic={}
lista=[]
while True:
    opcion=int(input("ingrese el numero de la opcion que desea realizar: "))
    if opcion==1:
        name=input("Ingrese su nombre: ")
        Cargo=input("Ingrese su cargo: ")
        Sueldo=float(input("Ingrese su salario: "))
        # dic=
        lista.append({1:name,2:Cargo,3:Sueldo})
    elif opcion==2:
        print(lista)
    elif opcion==3:
        break
    else:
        print("La opcion no es valida ")

