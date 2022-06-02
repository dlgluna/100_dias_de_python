#Versión 1
"""
def calculo_cada_tupla(lista: list):
    total = 0
    for data in lista:
        if type(data) is tuple:
            total += data[1] * data[2]
    if total < 600_000:
        total += 25_000
    print(f'La factura {lista[0]} tiene un total en pesos de {total:,.2f}')

def ordenes(rutinaContable):
    print('------------------------ Inicio Registro diario ---------------------------------')
    for registro in rutinaContable:
        calculo_cada_tupla(registro)
    print('-------------------------- Fin Registro diario ----------------------------------')
"""
#Versión 2
"""
def calculo_totales(lista: list):
    total = 0
    for i in range(1, len(lista)):
        total += lista[i][1] * lista[i][2]
    if total < 600_000:
        total += 25_000
    print(f'La factura {lista[0]} tiene un total en pesos de {total:,.2f}')

def ordenes(rutinaContable):
    print('------------------------ Inicio Registro diario ---------------------------------')
    for registro in rutinaContable:
        calculo_totales(registro)
    print('-------------------------- Fin Registro diario ----------------------------------')
"""

#Versión 3: funciones anónimas
"""
=> aqui se añade el código
"""

#Datos de prueba
registro_1 = [
        [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],
        [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
        [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
        [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]
]

registro_2 = [
[6587, ("3268", 4, 25842.99), ("8274",18,23254.99), ("6548", 9, 48951.95), ("2547", 5, 8951.95)],
[6588, ("1254", 3, 115362.58), ("9744", 2, 99235.66)],
]

registro_3 = [
[6589, ("9874", 1, 125698.20), ("88112", 2, 135645.20), ("3218", 4, 13645.20)],
[6590, ("5236", 8, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)],
[6591, ("7812", 2, 11.99), ("9652",11,18.99)],
]