#Parametros con valores por default (opcionales )

#Para documentar una funcion se unas las comillas simples 3 de apertura y 3 de cierre, por ejemplo en la funcion calculo_descuentos se documentara lo que hace 
#Lo cual nos beneficiara cuando mandemos a llamar a la funcion ya que nos dara una explicacion de lo que hace y lo que espera la funcion si recibe parametros


#Tambien puedo agregarle el valor de la variable que espero recibir en la funcion por ejemplo
#def calculo_descuentos(sueldo: float, isss: float=0.3, afp: float=0.0725):

def calculo_descuentos(sueldo, isss=0.3, afp=0.0725):
    '''
    Realiza el calculo de isss, afp y la suma de ambos apartir del sueldo \n
    el parametro del isss es opcional y el valor por default es 3% \n
    el parametro del afp es opcional y el valor por default es 7.25% \n
    el retorno es: isss, afp, suma
    '''

    desc_afp=sueldo*afp
    desc_isss=30
    if sueldo<=1000:
        desc_isss=sueldo*isss
    
    return desc_isss, desc_afp, desc_afp+desc_isss

desc1=calculo_descuentos(800)
print(f"Los descuentos son ISSS: {desc1[0]:.2f}, AFP {desc1[1]:.2f} y el total {desc1[2]:.2f}")

desc1=calculo_descuentos(800, 0.4)
print(f"Los descuentos son ISSS: {desc1[0]:.2f}, AFP {desc1[1]:.2f} y el total {desc1[2]:.2f}")

desc1=calculo_descuentos(800, 0.4, 1.0)
print(f"Los descuentos son ISSS: {desc1[0]:.2f}, AFP {desc1[1]:.2f} y el total {desc1[2]:.2f}")

desc1=calculo_descuentos(800, afp=1.2)
print(f"Los descuentos son ISSS: {desc1[0]:.2f}, AFP {desc1[1]:.2f} y el total {desc1[2]:.2f}")


calculo_descuentos()