#Programa para ver el funcionamiento de los diccionarios

Usuarios={"Usuario": "Marco",
        "Correo": "Marco12@gmail.com",
        "Token" : "kasda98da98da9sda8ujj"}

print(len(Usuarios))
print(Usuarios)
#Se accede por su llave
print(Usuarios["Usuario"])
print(Usuarios["Correo"])
print(Usuarios["Token"])
#Modificar el usuario
Usuarios["Usuario"]= "Alicia"
print(Usuarios)
#Agregar llave y valor al diccionario
Usuarios["Telefono"]="7788-8877"
print(Usuarios)
#Eliminar la key y el valor de token
Usuarios.pop("Token")
print(Usuarios)

print("---------------------------------------")
#Recorrer un diccionario por llave, valor o ambas(items)
print("Imprimiendo las llaves: ")
for key in Usuarios.keys():
    print(key)
print("--------------------")

print("Imprimiendo los valores: ")
for valor in Usuarios.values():
    print(valor)
print("--------------------")
print("Imprimiendo la llave y valor: ")
for key, valor in Usuarios.items():
    print(key, ":",valor)