# 6. Escribir un programa que vaya solicitando al usuario que ingrese nombres y telefonos.
# • Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar
# el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
# • Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente. El usuario
# puede utilizar la cadena "*", para salir del programa.

agenda={}
while True:
    Name = input("Ingrese un nombre (o '*' para salir): ")
    if Name == "*":
        break
    if Name in agenda:
        Phone_Number = agenda[Name]#Accedo al valor del nombre ingresado
        print(f"El teléfono de {Name} es {Phone_Number}.")    
        modificar = input("¿Desea modificar el teléfono? (s/n) ")
        if modificar.lower() == "s":
            Phone_Number = input("Ingrese el nuevo teléfono: ")
            agenda[Name] = Phone_Number
            print(f"El teléfono de {Name} ha sido actualizado.")
    else:
        Phone_Number = input(f"Ingrese el teléfono de {Name}: ")
        agenda[Name] = Phone_Number #Ingreso un numero de telefono a la clave nombre 
        print(f"El teléfono de {Name} ha sido agregado a la agenda.")

print("Agenda actualizada:")
for Name, Phone_Number in agenda.items():
    print(f"{Name}: {Phone_Number}")
