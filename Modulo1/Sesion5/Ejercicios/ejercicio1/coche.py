from motor import Motor
from rueda import Rueda
from puerta import Puerta

class Coche:
    def __init__(self):
        self.motor = Motor()
        self.ruedas = [Rueda() for i in range(4)]
        self.puertas = [Puerta() for i in range(2)]
        
    def encender_coche(self):
        self.motor.arrancar()
        
    def apagar_coche(self):
        self.motor.apagar()
        
    def inflar_ruedas(self):
        for rueda in self.ruedas:
            rueda.inflar()
            
    def desinflar_ruedas(self):
        for rueda in self.ruedas:
            rueda.desinflar()
            
    def abrir_puertas(self):
        for puerta in self.puertas:
            puerta.abrir()
            
    def cerrar_puertas(self):
        for puerta in self.puertas:
            puerta.cerrar()