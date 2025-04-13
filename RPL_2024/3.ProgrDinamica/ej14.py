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

def calculoOptimos(ganancia):
    optimosConPrimera = [0] * (len(ganancia))
    optimosConPrimera[0] = 0
    optimosConPrimera[1] = ganancia[0]

    optimosSinPrimera = [0] * (len(ganancia))
    optimosSinPrimera[0] = 0
    optimosSinPrimera[1] = ganancia[1]

    for i in range(1,len(ganancia)-1):
        optimosConPrimera[i+1] = max(ganancia[i] + optimosConPrimera[i-1], optimosConPrimera[i])
        optimosSinPrimera[i+1] = max(ganancia[i+1] + optimosSinPrimera[i-1], optimosSinPrimera[i])

    if optimosConPrimera[-1] >= optimosSinPrimera[-1]:
        return optimosConPrimera, 0,len(ganancia)-1
    else:
        return optimosSinPrimera, 1,len(ganancia)

def invertirOptimo(ganancias,inicio,fin,pos,optimos,numeroCasas):
    if pos < inicio or pos == 0 or fin < inicio:
        return numeroCasas
    
    if optimos[pos] == optimos[pos-1]:
        return invertirOptimo(ganancias,inicio,fin-1,pos-1,optimos,numeroCasas)
    else:
        numeroCasas.append(fin-1)
        return invertirOptimo(ganancias,inicio,fin-2,pos-2,optimos,numeroCasas)

def lunatico(ganancias):
    if not ganancias:
        return []
    if len(ganancias) == 1:
        return [0]
    #Ecuacion Recurrencia -> gan[i] = max( casa[i] + opt[i-2] , opt[i-1] )
    numeroCasas = []

    optimos, inicio, fin = calculoOptimos(ganancias)

    invertirOptimo(ganancias,inicio,fin,len(optimos)-1,optimos,numeroCasas)

    numeroCasas = list(reversed(numeroCasas))
    
    return numeroCasas
#O(n)

# Definir un arreglo de ganancias
ganancias = [20, 15, 300]

# Llamar a la función lunatico con el arreglo de ganancias
resultado = lunatico(ganancias)

# Imprimir el resultado obtenido
print(resultado)

"""
[]

[10]

[20, 15]

[10, 15]

[100, 150, 100]

[10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100]

[50, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100, 10, 100]

[100, 20, 30, 70, 50]

[100, 20, 70, 70, 120]

[21, 78, 68, 95, 30]

[38, 61, 84, 87, 93, 56, 99, 97, 47, 28, 94, 65, 19, 17, 91, 23, 18, 1, 53, 21, 10, 13, 21, 78, 68, 95, 30, 4, 44, 22, 11, 77, 52, 68, 18, 31]
"""