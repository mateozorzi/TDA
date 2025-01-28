def calculoOptimos(monedas,W):
    optimos = [[1] * (W+1) for i in range(len(monedas)+1)]

    #caso base, todos los cambios con la moneda de valor 1, solo tengo una opcion
    for i in range(1,len(optimos[1])):
        optimos[1][i] = 1

    #caso base, cuando tengo que dar cambio de 1, para todas las monedas solo tengo una opcion
    for j in range(1,len(optimos)):
        optimos[j][1] = 1

    for cantMonedas in range(2,len(optimos)): #O(monedas)
        for monto in range(2,len(optimos[cantMonedas])): #O(W)
            if monto < monedas[cantMonedas-1]:
                optimos[cantMonedas][monto] = optimos[cantMonedas-1][monto]
            else:
                optimos[cantMonedas][monto] = optimos[cantMonedas-1][monto] + optimos[cantMonedas][monto - monedas[cantMonedas-1]]

    return optimos


def monedasDistintas(monedas, W):
    optimos = calculoOptimos(monedas,W) #O(monedas*W)
    
    return optimos[-1][-1] #O(1)
#complejidad O(monedas*W)


monedas = [1,2,5,10,20,100,200,1000]
print(monedasDistintas(monedas,30))
    