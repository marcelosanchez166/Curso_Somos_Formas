# 1. Verificar si una palabra es palíndroma (invierta la cadena con un while o for)


palabra=input('Dime una palabra: ').lower()
es=True
for i in range(len(palabra)):
    if palabra[i]!=palabra[len(palabra)-i-1]:
        es=False
if es:
    print('Si es un palíndromo')
else:
    print('No es un palíndromo')























# palabra=input("ingrese una palabra: ")
# pali=[]
# for i in range(len(palabra)):
#     pali.append(palabra[i])
# print(pali)
# if pali==palabra:
#     print("La palabra que ingreso", pali,"Si es palindromo")
# else:
#     print("No es palindromo")



