def en_rango(numero, rango_min, rango_max):
    if rango_min <= numero <= rango_max:
        return True
    else:
        return False


numero = 7
minimo = 9
maximo = 27

if en_rango(numero, minimo, maximo):
    print(f"{numero} está en el rango de {minimo} a {maximo}.")
else:
    print(f"{numero} no está en el rango de {minimo} a {maximo}.")
