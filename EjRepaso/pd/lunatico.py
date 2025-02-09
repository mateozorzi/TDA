"""Somos ayudantes del gran ladrón el Lunático, que está pensando en su próximo atraco. 
Decidió en este caso robar toda una calle en un barrio privado, que tiene la particularidad de ser circular. 
Gracias a los trabajos de inteligencia realizados, sabemos cuánto se puede obtener por robar en cada casa. 
Podemos enumerar a la primer casa como la casa 0, de la cual podríamos obtener g0, 
la casa a su derecha es la 1, que nos daría g1, y así hasta llegar a la casa n-1, que nos daría gn-1. 
Toda casa se considera adyacente a las casas i-1 e i+1. Además, como la calle es circular, la casas 0 y n-1 también son vecinas. 
El problema con el que cuenta el Lunático es que sabe de experiencias anteriores que, 
si roba en una casa, los vecinos directos se enterarían muy rápido. No le daría tiempo a luego intentar robarles a ellos. 
Es decir, para robar una casa debe prescindir de robarle a sus vecinos directos. 
El Lunático nos encarga saber cuáles casas debería atracar y cuál sería la ganancia máxima obtenible. 
Dado que nosotros nos llevamos un porcentaje de dicha ganancia, vamos a buscar el óptimo a este problema. 
Implementar un algoritmo que, por programación dinámica, obtenga 
la ganancia óptima, así como cuáles casas habría que robar, a partir de recibir un arreglo de las ganancias obtenibles. 
Para esto, escribir y describir la ecuación de recurrencia correspondiente. Indicar y justificar la complejidad del algoritmo propuesto."""

def buscarOptimos(casas):
    optimosPrimera = [0] * (len(casas))
    optimosPrimera[1] = casas[0]

    for i in range(2,len(optimosPrimera)):
        optimosPrimera[i] = max(optimosPrimera[i-1], optimosPrimera[i-2] + casas[i-1])

    optimosUltima = [0] * (len(casas))
    optimosUltima[1] = casas[1]
    for j in range(2, len(optimosUltima)):
        optimosUltima[j] = max(optimosUltima[j-1], optimosUltima[j-2] + casas[j])
    
    if optimosPrimera[-1] > optimosUltima[-1]:
        return optimosPrimera, len(casas)-1

    return optimosUltima, len(casas)

def reconstruccion(casas, optimos, pos,numero, solucion):
    if pos <= 0:
        return solucion
    
    if optimos[pos-1] == optimos[pos]:
        return reconstruccion(casas, optimos, pos-1,numero-1, solucion)
    else:    
        solucion.append(numero-1)
        return reconstruccion(casas, optimos, pos-2,numero-2, solucion)

def lunatico(casas):
    optimos, numero = buscarOptimos(casas)

    solucion = []
    solucion = reconstruccion(casas, optimos, len(optimos)-1, numero, solucion)
    solucion = list(reversed(solucion))

    return solucion

casas =  [100, 150, 200]
print(lunatico(casas))