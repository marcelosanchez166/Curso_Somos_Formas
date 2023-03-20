# 3. Contar palabras en una cadena

palabra=input("Ingrese una palabra: ")
# palabra=int(palabra)
count=0

for i in range (len(palabra)):
    count=i+1
print("La palabra tiene", count, "letras")