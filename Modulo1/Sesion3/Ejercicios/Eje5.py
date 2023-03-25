# 5. Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de
# apariciones de cada palabra en la cadena. Por ejemplo, si recibe "Qué lindo día que hace hoy" debe
# devolver: 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1


def contar_palabras(cadena):
# Convertir a minúsculas y eliminar signos de puntuación
    cadena = cadena.lower().replace(",", "").replace(".", "").replace(";", "").replace(":", "")
    # Separar las palabras en una lista
    palabras = cadena.split()
    # Crear un diccionario vacío para contar las apariciones
    apariciones = {}
    # Iterar sobre las palabras y contar las apariciones
    for palabra in palabras:
        if palabra in apariciones:
            apariciones[palabra] += 1
        else:
            apariciones[palabra] = 1
    # Devolver el diccionario con las apariciones
    return apariciones

print(contar_palabras("Hola como estas, Hola mi nombre es Luis, como te llamas, te llamas Luis tambien"))