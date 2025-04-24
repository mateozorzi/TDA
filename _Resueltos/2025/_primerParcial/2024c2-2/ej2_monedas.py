"""
Implementar un algoritmo que, utilizando backtracking, resuelva el problema del cambio (obtener la forma de dar
cambio en la mínima cantidad de monedas) con una nueva restricción: no se tiene una cantidad indefinida de cada
moneda, sino una cantidad específica (y esto hace que pueda no haber solución). Suponer que la función a invocar
es cambio(n, monedas, cantidad_x_monedas), donde n sea el valor a devolver en cambio, monedas sea una lista
ordenada de los valores de las monedas, y cantidad_x_monedas un diccionario
"""

def cambio(n, monedas, cantidad_x_monedas, indice, parcial, sol):
    if sum(parcial) == n and len(parcial) < len(sol):
        return parcial[:]
    
    if indice >= len(monedas):
        return sol
    
    if sum(parcial) + (monedas[i] * cantidad_x_monedas[i] for i in range(indice, len(monedas))):
        return sol
    
    if cantidad_x_monedas[indice] > 0 and n >= monedas[indice]:
        parcial.append(monedas[indice]) #agrego la moneda a la sol
        cantidad_x_monedas[indice] -= 1 #disminuyo en 1 la cantidad de la moneda

        if cantidad_x_monedas[indice] > 0 and n-monedas[indice] >= monedas[indice]:
            sol = cambio(n, monedas, cantidad_x_monedas, indice, parcial, sol)
        else:
            #si no me quedan monedas, o no puedo agregar otra de estas monedas
            sol = cambio(n, monedas, cantidad_x_monedas, indice+1, parcial, sol)
        
        parcial.pop()
        cantidad_x_monedas[indice] += 1
    sol = cambio(n, monedas, cantidad_x_monedas, indice+1, parcial, sol)

    return sol

        

        

def cambio(n, monedas, cantidad_x_monedas):
    parcial = []
    sol = []

    indice = 0

    sol = cambio(n, monedas, cantidad_x_monedas, indice, parcial, sol)

    return sol