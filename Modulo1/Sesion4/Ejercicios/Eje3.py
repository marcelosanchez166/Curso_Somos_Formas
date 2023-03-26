# 3. Escribir la función titulo(), la cual recibe un string y lo retorna convirtiendo la
# primera letra de cada palabra a mayúscula y las demás letras a minúscula,
# dejando inalterados los demás caracteres. Precondición: el separador de
# palabras es el espacio: " ". No usar la función title de Python.

lista=[]
def titulo(cadena):
    cadena = cadena.lower().replace(",", "").replace(".", "").replace(";", "").replace(":", "")
    palabras = cadena.split()
    for palabra in palabras:
        new_word = palabra[0].upper() + palabra[1:].lower()  # convierte la primera letra en mayúscula y el resto en minúscula
        lista.append(new_word)
    return " ".join(lista)

print(titulo("Hola cOmo estAs, espeRo que bien CUIDATE Mucho, saludos"))