def AutoPartes(ventas:list):
    resultado = {}
    for i in range(len(ventas)):
        for j in range(len(ventas[0])):
            resultado[i] = ventas[i]

    return resultado

def consultaRegistro(ventas, idProducto):
    contador = 0
    for valor in ventas.values():
        if valor[0] == idProducto:
            print(f"Producto consultado : {idProducto}  Descripción  {valor[1]}  #Parte  {valor[2]}  Cantidad vendida  {valor[3]}  Stock  {valor[4]}  Comprador {valor[5]}  Documento  {valor[6]}  Fecha Venta  {valor[7]}")
        if valor[0] != idProducto:
            contador +=1
            if contador >= len(ventas):
                print('No hay registro de venta de ese producto')
                

#datos de prueba
"""
consultaRegistro(AutoPartes([
    (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
    (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
    (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),    
    (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
    (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010)
print()
Producto consultado : 2010  Descripción  bujía  #Parte  MS9512  Cantidad vendida  4  Stock  15  Comprador Carlos Rondon  Documento  1256  Fecha Venta  12/06/2020
Producto consultado : 2010  Descripción  bujía  #Parte  ER6523  Cantidad vendida  9  Stock  36  Comprador Pedro Montes  Documento  1243  Fecha Venta  12/06/2020

consultaRegistro(AutoPartes([
    (5489,'tornillo', 'RS8512',2,33,'Julio Perez',3654213,'13/06/2020'),
    (3215,'zocalo', 'UM8587',2,125,'Laura Macias',1256321,'13/06/2020'),
    (3698,'biela', 'PT3218',1,78,'Luis Peña',14565487,'13/06/2020'),
    (8795,'cilindro', 'AZ8794',2,96,'Carlos Casio',5612405,'13/06/2020')]), 2001)
print()
No hay registro de venta de ese producto

consultaRegistro(AutoPartes([
    (9852,'Culata', 'XC9875',2,165,'Luis Molero',3455846,'14/06/2020'),
    (9852,'Culata', 'XC9875',2,165,'Jose Mejia',1355846,'14/06/2020'),
    (2564,'Cárter', 'PT29872',2,32,'Peter Cerezo',8545436,'14/06/2020'),
    (5412,'válvula', 'AZ8798',2,11,'Juan Peña',568975,'14/06/2020')]), 9852)
print()
Producto consultado : 9852  Descripción  Culata  #Parte  XC9875  Cantidad vendida  2  Stock  165  Comprador Luis Molero  Documento  3455846  Fecha Venta  14/06/2020
Producto consultado : 9852  Descripción  Culata  #Parte  XC9875  Cantidad vendida  2  Stock  165  Comprador Jose Mejia  Documento  1355846  Fecha Venta  14/06/2020

consultaRegistro(AutoPartes([
    (9852,'Culata', 'XC9875',2,165,'Luis Molero',3455846,'15/06/2020'),
    (9852,'Culata', 'XC9875',2,165,'Jose Mejia',1355846,'15/06/2020'),
    (2564,'Cárter', 'PT29872',2,32,'Peter Cerezo',8545436,'15/06/2020'),
    (5412,'válvula', 'AZ8798',2,11,'Juan Peña',568975,'15/06/2020')]), 2564)
print()
Producto consultado : 2564  Descripción  Cárter  #Parte  PT29872  Cantidad vendida  2  Stock  32  Comprador Peter Cerezo  Documento 8545436  Fecha Venta  15/06/2020

consultaRegistro(AutoPartes([
    (2564,'Cárter', 'PT29872',2,32,'Peter Cerezo',8545436,'16/06/2020'),
    (5412,'válvula', 'AZ8798',2,11,'Juan Peña',568975,'16/06/2020')]), 5412)
print()
Producto consultado : 5412  Descripción  válvula  #Parte  AZ8798  Cantidad vendida  2  Stock  11  Comprador Juan Peña  Documento  568975  Fecha Venta  16/06/2020

consultaRegistro(AutoPartes([
    (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'17/06/2020'),
    (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'17/06/2020'),    
    (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'17/06/2020')]), 2085)
print()
No hay registro de venta de ese producto

"""