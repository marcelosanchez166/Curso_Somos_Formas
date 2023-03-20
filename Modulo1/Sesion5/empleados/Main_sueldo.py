from Class_empleados import Empleado, EmpleadoPorComision, EmpleadoPorHora

employe1=Empleado("Julia",12312)
employe2=EmpleadoPorComision("Neto",13444402,6000)
employe3=EmpleadoPorHora("Julia",998822,40, 5)

print(employe1.Calcular_sueldo())
print(employe2.Calcular_sueldo())
print(employe3.Calcular_sueldo())


if isinstance(employe1, Empleado):
    print ("OK")
if isinstance(employe2, Empleado):
    print ("OK")
if isinstance(employe3, Empleado):
    print ("OK")
