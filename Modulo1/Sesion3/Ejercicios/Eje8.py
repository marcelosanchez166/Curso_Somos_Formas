# 8. Escribe una función llamada "elimina_duplicados" que tome una lista y devuelva una nueva lista(Sin los elementos duplicados)
# con los elementos únicos de la lista original. No tienen por qué estar en el mismo orden.

lista_sin_duplicados=[]
def elimina_duplicado(lista1):
    for i in range(len(lista1)):
        if lista1[i] not in lista_sin_duplicados:
            lista_sin_duplicados.append(lista1[i])


elimina_duplicado([3,4,5,4,3,7,77,7,6,6,5,4,2,11,1,1,0])

print(lista_sin_duplicados)