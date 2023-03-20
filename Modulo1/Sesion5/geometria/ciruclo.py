from geometria.figura import Figura

class Circulo(Figura):#Esta clase esta heredando de la clase padre que es Figura que esta en el archivo figura.py
    def __init__(self, nombre, radio):#constructor de la clase Circulo
        super().__init__(nombre)#Constructor de la clase Padre Figura del archivo figura.py
        self.PI=3.1415
        self.radio=radio
    
    def Calcular_area(self):
        return self.PI *(self.radio**2)
    
    def Calcular_perimetro(self):
        return 2*self.PI*self.radio