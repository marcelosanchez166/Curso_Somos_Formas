#El polimorfismo consiste en sobreescribir metodos como en este caso estamos sobreescribiendo el metodo Calcular_sueldo ya que este viene heredado de la clase Empleado
#Por lo tanto cuando creamos un nuevo metodo con ese nombre nos sugiere usar el Metodo de la clase padre que es la de Empleado, pero en este caso solo hacemos uso del nombre
#para realizar otras acciones y no la que tiene por defecto dada en la clase empleado

class Empleado:
    def __init__(self, Nombre, NIT):
        self.Nombre=Nombre
        self.NIT=NIT
    
    def Calcular_sueldo(self):
        return 1000
    
class EmpleadoPorComision(Empleado):
    
    def __init__(self, Nombre, NIT, Ventas):
        super().__init__(Nombre, NIT)
        self.Ventas=Ventas
    
    def Calcular_sueldo(self):
        return self.Ventas*0.2
    
class EmpleadoPorHora(Empleado):
    def __init__(self, Nombre, NIT, Horas_trabajadas, Horas_extras):
        super().__init__(Nombre, NIT)
        self.Horas_trabajadas=Horas_trabajadas
        self.Horas_extras=Horas_extras
    
    def Calcular_sueldo(self):
        return self.Horas_trabajadas*10+ self.Horas_extras*2*10


