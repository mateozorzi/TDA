def cambio(monedas, monto):
    #Regla greedy: ordenar las monedas de mayor a menor
    #iterar sobre las monedas, primero elgiendo la de mas valor
    #y asi ir cumpliendo el cambio
    #Es greedy porque para cada iteracion utiliza la moneda de mayor denominacion que pueda usar para dar cambio, optimo local.

    monedas = sorted(monedas, reverse=True)
    indice = 0

    cambio = []

    while indice < len(monedas) and monto > 0:
        if monedas[indice] <= monto:
            monto -= monedas[indice]
            cambio.append(monedas[indice])
        else: #monedas[indice] > monto
            indice += 1

    return cambio

#No es optimo para todos los casos, por ejemplo para el caso
# [13,9,7,1] y un monto de 16, el algoritmo greedy devolvera 
# [13,1,1,1], cuando el optimo hubiera sido [9,7]


mon = [13,7,9,1]
print(cambio(mon,16))