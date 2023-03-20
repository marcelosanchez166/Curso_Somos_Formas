from procesos import planilla
from utilerias.util import limpiar, MENU

while True:
    print(MENU)
    opcion=int(input("Digite una opcion: "))


    if opcion<1 or opcion>6:
        break

    sueldo=float(input("Digite su sueldo: "))
    match opcion:
        case 1:
            print(f"El ISSS es:  {planilla.isss(sueldo):.2f}")
        case 2:
            print(f"El AFP es:  {planilla.afp(sueldo):.2f}")
        case 3:
            print(f"El Sueldo Gravable es:  {planilla.sueldo_gravable(sueldo):.2f}")            
        case 4:
            print(f"El ISR es:  {planilla.isr(sueldo):.2f}")
        case 5:
            print(f"El total de descuentos es:  {planilla.total_descuentos(sueldo):.2f}")
        case 6:
            print(f"El sueldo a pagar es:  {planilla.sueldo_pagar(sueldo):.2f}")
    
    input()
    limpiar()

