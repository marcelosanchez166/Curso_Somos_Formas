# 5. Una inmobiliaria de una ciudad maneja una lista de inmuebles como la
# siguiente:
# [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona':
# 'A'},
# {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona':
# 'B'},
# {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona':
# 'A'},
# {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona':
# 'B'},
# {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona':
# 'A'}]
# Construir una función que permita hacer búsqueda de inmuebles en función de un
# presupuesto dado. La función recibirá como entrada la lista de inmuebles y un
# precio, y devolverá otra lista con los inmuebles cuyo precio sea menor o igual que
# el dado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo par
# a cada diccionario con el precio del inmueble, donde el precio de un inmueble se
# calcula con la siguiente fórmula en función de la zona:
# • Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-
# antiguedad/100)
# • Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-
# antiguedad/100) * 1.5

def buscar_inmuebles(lista_inmuebles, Presupuesto):
    inmuebles_encontrados = []
    for inmueble in lista_inmuebles:
        print(inmueble)
        precio = 0
        if inmueble['zona'] == 'A':
            precio = (inmueble['metros'] * 1000 + inmueble['habitaciones'] * 5000 + inmueble['garaje'] * 15000) * (1 - (2023 - inmueble['año'])/100)
            print("Zona A",precio)
        elif inmueble['zona'] == 'B':
            precio = (inmueble['metros'] * 1000 + inmueble['habitaciones'] * 5000 + inmueble['garaje'] * 15000) * (1 - (2023 - inmueble['año'])/100) * 1.5
            print("Zona A",precio)
        if precio <= Presupuesto:
            inmueble['precio'] = precio
            inmuebles_encontrados.append(inmueble)
    return inmuebles_encontrados

lista_inmuebles = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona':'A'},
                {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona':'B'},
                {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona':'A'},
                {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona':'B'},
                {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona':'A'}]

Presupuesto=float(input("Cuanto es su presupuesto para comprar el inmueble "))
inmuebles_encontrados = buscar_inmuebles(lista_inmuebles,Presupuesto)
print(inmuebles_encontrados)














# inmuebles_dentro_de_presupuesto=[]
# def buscar_inmuebles(lista_inmuebles,Presupuesto):
#     Zona_A_precio = (lista_inmuebles[0]["metros"] * 1000 + lista_inmuebles[0]["habitaciones"] * 5000 + lista_inmuebles[0]["garage"] * 15000) * (1-lista_inmuebles[0]["year"]/100)
#     Zona_B_precio = (lista_inmuebles[0]["metros"] * 1000 + lista_inmuebles[0]["habitaciones"] * 5000 + lista_inmuebles[0]["garage"] * 15000) * (1-lista_inmuebles[0]["year"]/100) * 1.5
        
#     if Presupuesto <=Zona_A_precio:
#         lista_inmuebles_ordenadas.append()
    
#     elif Presupuesto <=Zona_B_precio:
#         lista_inmuebles_ordenadas.append()
