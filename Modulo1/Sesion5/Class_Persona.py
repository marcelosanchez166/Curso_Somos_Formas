#El proposito de los atributos y las funcionones y es ser usados dentro de la misma clase a o las clases hijas

class Persona:
    def __init__(self, nombre, apellido, dui, edad):
        self.nombre=nombre
        self._apellido=apellido
        self.__dui=dui
        self.__edad=edad


    def __es_adulto(self):
        return self.__edad>=18

    def mostrar_datos(self):
        print(
            f"Nombre: {self.nombre}\n"
            f"Apellido: {self._apellido}\n"
            f"DUI: {self.__dui}, Adulto: {self.__es_adulto()}\n"
            f"Edad: {self.__edad}\n"
            f"-----------------------------------------------"
        )


# p1=Persona("Alicia", "Lopez", "122-6",15)
# p1.mostrar_datos()

