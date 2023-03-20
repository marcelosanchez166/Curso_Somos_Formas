#Los scripts son los que ejecutan tareas(Instrucciones) y los modulos son los que tienen informacion y son llamados por los scripts 

#Los atributos privados no son accesibles desde afuera de ningun lado
#Los atributos protegidos si son accesibles ya que no tienen una proteccion forzosa

from Class_Persona import Persona


#instanciando la clase persona
alicia= Persona("Alicia", "Lopez", "05186498-6",15)
Beto=Persona("Beto", "Lopez", "05186498-6",15)



#atributos publicos, imprimiendo solo el atributo nombre de la clase 
#print(f"Nombre en objeto 1: {alicia.nombre}")

#atributos protegidos, imprimiendo solo el atributo apellido de la clase 
#print(f"Apellido en objeto 1: {alicia._apellido}")


#atributos privados
#print(f"Apellido en objeto 1: {alicia.__edad}")
print(f"Apellido en objeto 1: {alicia.__dui}")

#Metodos publicos, de esta forma puedo obtener todos los atributos de la clase
alicia.mostrar_datos()
Beto.mostrar_datos()


