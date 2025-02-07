def cambio_bt(n, monedas, cantidadMonedas, indice,parcial, sol):
    if len(sol) == 0 and sum(parcial) == n:
        sol = parcial.copy()
        return sol
    
    if len(parcial) < len(sol) and sum(parcial) == n:
        sol = parcial.copy()
        return sol

    if cantidadMonedas[indice] > 0 and monedas[indice] <= (n - sum(parcial)):
        parcial.append(monedas[indice])
        cantidadMonedas[monedas[indice]] -= 1 #resto uno a la cantidad de monedas
        if cantidadMonedas[indice] > 0 and (n - sum(parcial)) >= monedas[indice]:
            #entra otra monedas[indice]
            sol = cambio_bt(n, monedas, cantidadMonedas, indice, parcial, sol)
        else:
            #no entran mas de monedas[indice]
            sol = cambio_bt(n, monedas, cantidadMonedas, indice+1, parcial,sol)
        
        parcial.pop()
        cantidadMonedas[monedas[indice]] += 1
    sol = cambio_bt(n, monedas, cantidadMonedas, indice+1, parcial,sol)

    #si llego aca, no hay solucion
    return None

#n -> cambio a dar
#monedas -> lista de monedas
#cantidad_x_monedas -> dict con la cantidad de monedas restantes
def cambio(n, monedas, cantidad_x_monedas):
    sol = []
    parcial = []
    indice = 0
    monedas = sorted(monedas, reverse=True)

    sol = cambio_bt(n, monedas, cantidad_x_monedas, indice, parcial,sol)

    return sol