# 2. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje
# indicando si la dirección es válida o no, valiéndose de una función para
# decidirlo. Una dirección se considerará válida si contiene el símbolo "@".

def correo(email):
    if "@" in email:
        return "La direccion de correo es valida"
    return "El correo es invalido"

print(correo("marcelosanchez166gmail.com"))