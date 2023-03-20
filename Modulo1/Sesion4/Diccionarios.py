#Programa para ver uso de diccionarios, ejemplo acceder a los roles del usuario que se agregaron a la lista, mostrar el email del usuario que esta dentro del diccionario en la lista
u1={
    "id": 1,
    "Usuario":"alicia",
    "Correo": "Alicio@gmail.com",
    "Token": "dssdfsdfsdtswerr23asfw3rsdfgshgdhjddfasahye",
    "rol": {1:"Gerente", 2:"Admin"}
}

lista=[]
lista.append(u1)

for key,valor in lista[0]["rol"].items():
    print( key, valor)
