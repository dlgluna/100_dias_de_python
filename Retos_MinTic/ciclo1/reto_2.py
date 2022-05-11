def cliente(informacion: dict)->dict:
    resultado = {}
    name = informacion['nombre']
    age = informacion['edad']
    f_access = informacion['primer_ingreso']

    apto = True

    if age > 18:
        atraccion = 'X-Treme'
        if f_access:
            total_boleta = 20000 - (20000 * 5 / 100)
        else:
            total_boleta = 20000
    elif age >= 15 and age <= 18:
        atraccion = 'Carros chocones'
        if f_access:
            total_boleta = 5000 - (5000 * 7 / 100)
        else:
            total_boleta = 5000
    elif age >= 7 and age < 15:
        atraccion = 'Sillas voladoras'
        if f_access:
            total_boleta = 10000 - (10000 * 5 / 100)
        else:
            total_boleta = 10000
    else:
        atraccion = 'N/A'
        apto = False
        total_boleta = 'N/A'

    resultado['nombre'] = name
    resultado['edad'] = age
    resultado['atraccion'] = atraccion
    resultado['apto'] = apto
    resultado['primer_ingreso'] = f_access
    resultado['total_boleta'] = total_boleta


    return resultado


informacion = {
    'id_cliente': 1,
    'nombre': 'Johana Fernandez',
    'edad': 20,
    'primer_ingreso': True
}
print(cliente(informacion))

informacion = {
    'id_cliente': 1,
    'nombre': 'Johana Fernandez',
    'edad': 20,
    'primer_ingreso': False

}

print(cliente(informacion))