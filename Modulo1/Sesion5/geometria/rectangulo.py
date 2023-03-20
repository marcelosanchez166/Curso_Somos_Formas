from geometria.figura import Figura

class Rectangulo(Figura):#Esta clase esta heredando de la clase padre que es Figura que esta en el archivo figura.py
    def __init__(self, nombre,base, altura):#constructor de la clase Rectangulo
        super().__init__(nombre)#Constructor de la clase Padre Figura del archivo figura.py
        self.base=base
        self.altura=altura
    
    def Calcular_area(self):
        return self.base*self.altura
    
    def Calcular_perimetro(self):
        return 2*(self.base+self.altura)

