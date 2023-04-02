from ventana import Ventana

class Puerta:
    def __init__(self):
        self.ventana = Ventana()
        
    def abrir(self):
        print("La puerta se ha abierto.")
        self.ventana.abrir()
        
    def cerrar(self):
        print("La puerta se ha cerrado.")
        self.ventana.cerrar()