# 3. Escribir una clase llamada Persona que siga las siguientes condiciones:
# ▪ Sus atributos son: nombre, edad, DUI, sexo (H hombre, M mujer), peso y
# altura. No queremos que se accedan directamente a ellos. Piensa que
# modificador de acceso es el más adecuado, también su tipo.
# ▪ Por defecto, todos los atributos menos el DUI serán valores por defecto según su
# tipo (0 números, cadena vacía para String, etc.). Sexo será hombre por defecto.
# ▪ Los métodos que se implementaran son:
# ▪ calcularIMC(): calculará si la persona está en su peso ideal (peso en
# kg/(altura^2 en m)), si esta fórmula devuelve un valor menor que 20, la
# función devuelve un -1, si devuelve un número entre 20 y 25 (incluidos),
# significa que está por debajo de su peso ideal la función devuelve un 0 y si
# devuelve un valor mayor que 25 significa que tiene sobrepeso, la función
# devuelve un 1. Se recomienda usar constantes para devolver estos valores.
# ▪ esMayorDeEdad(): indica si es mayor de edad, devuelve un booleano.
# ▪ comprobarSexo(sexo): comprueba que el sexo introducido es correcto(H
# 0 M). Si no es correcto, será H. No será visible al exterior.
# ▪ __str__(): devuelve toda la información del objeto.
# ▪ generaDUI(): genera un número aleatorio de 9 cifras. Este método será
# invocado cuando se construya el objeto. No será visible al exterior
# Ahora, crea un programa principal que haga lo siguiente:
# ▪ Pide por teclado los datos de N personas: nombre, la edad, sexo, peso y altura.
# ▪ Crea 1 objeto por cada persona de la clase anterior con los datos y agrégalos a
# una lista de objetos persona
# ▪ Para cada objeto, deberá comprobar si está en su peso ideal, tiene sobrepeso o
# por debajo de su peso ideal con un mensaje.
# ▪ Indicar en cada objeto si es mayor de edad.
# ▪ Por último, mostrar la información de cada objeto.
# Es posible usar funciones en el programa principal, para que sea más fácil.