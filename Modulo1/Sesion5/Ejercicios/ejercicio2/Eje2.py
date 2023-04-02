# 2. Crea una clase llamada Cuenta que tendrá los siguientes atributos: cliente y
# cantidad (puede tener decimales).
# • El cliente será obligatorio y la cantidad es opcional.
# Tendrá tres métodos:
# ▪ ingresar (float cantidad): se ingresa una cantidad a la cuenta, si la cantidad
# introducida es negativa, no se hará nada.
# ▪ retirar (float cantidad): se retira una cantidad a la cuenta, si restando la cantidad
# actual a la que nos pasan es negativa, la cantidad de la cuenta pasa a ser 0.
# ▪ consultarSaldo: imprime el saldo de la cuenta

class Cuenta():
    def __init__(self,cliente,cantidad=1000):
        self.estadoCuenta=0
        self.cliente=cliente
        self.cantidad=cantidad


    def ingresar(self,deposito):
        if deposito<0:
            pass
        else:
            self.estadoCuenta+=deposito
            return "Su estado de cuenta actual es: ", self.estadoCuenta

    def retirar(self,retiro):
        if retiro>self.estadoCuenta:
            return 0
    
    def consultarSaldo(self):
        return self.estadoCuenta

deposito=float(input("Ingrese la cantidad a depositar: "))
nombre=input("Ingrese su nombre: ")
cuenta1=Cuenta(nombre)
print(cuenta1.ingresar(deposito))

retiro=float(input("Ingrese la cantidad a retirar: "))
nombre=input("Ingrese su nombre: ")
cuenta2=Cuenta(nombre)
print(cuenta2.retirar(retiro))
#lista.append({1:name,2:Cargo,3:Sueldo})