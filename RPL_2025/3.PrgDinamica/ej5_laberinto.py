"""
Dado un laberinto representado por una grilla, queremos calcular la ganancia máxima que existe desde la posición (0,0) hasta la posición NxM. Los movimientos permitidos son, desde la esquina superior izquierda (el (0,0)), nos podemos mover hacia abajo o hacia la derecha. Pasar por un casillero determinado (i, j) nos da una ganancia de V_{i,j}. Implementar un algoritmo que, por programación dinámica, obtenga la máxima ganancia a través del laberinto. Hacer una reconstrucción del camino que se debe transitar. Indicar y justificar la complejidad del algoritmo implementado. Si hay algunos lugares por los que no podemos pasar (obstáculos), ¿cómo se debe modificar para resolver el mismo problema?

Aclaración: solamente por simplicidad de las pruebas automáticas, devolver en este caso la ganancia máxima obtenible. Tener en cuenta que en un examen se pediría la reconstrucción de cómo se obtiene la ganancia.
"""

#ec de recurrencia, debo ver si conviene ir hacia abajo o hacia la derecha. para el casillero (i,j) me quedare del mejor camino,
# que puede ser venir de (i-i,j) o de (i, j-1)
def buscarOptimos(matriz):
    fil = len(matriz)
    col = len(matriz[0])

    optimos = [[0] * (col+1) for _ in range(fil+1)]

    #Ec de recurrecnia: -> opt[i][j] = max(opt[i-1][j], opt[i][j-1])
    for i in range(1,len(optimos)):
        for j in range(1, len(optimos[0])):
            #si hay obstaculos:
            if matriz[i-1][j-1] == 0:
                optimos[i][j] = 0
                continue
            if optimos[i-1][j] == 0 and  optimos[i][j-1] == 0 and (i,j) != (1,1):
                optimos[i][j] = 0
                continue
            optimos[i][j] = max(optimos[i-1][j], optimos[i][j-1]) + matriz[i-1][j-1]

    #la rta optima estara en el casillero i = n, j = m
    return optimos

def reconstruccion(matriz, optimos, i, j):
    sol = []
    sol.append((i,j))

    while i >= 1 and j >= 1:
        if optimos[i][j] == optimos[i-1][j]:
            #vine desde arriba
            sol.append((i-1,j))
            i -= 1
        else:
            #vinde desde la izq
            sol.append((i,j-1))
            j -= 1
    
    return sol

def laberinto(matriz):
    optimos = buscarOptimos(matriz)
    
    sol = reconstruccion(matriz, optimos, len(optimos)-1, len(optimos[0])-1)
    
    return optimos[len(optimos), len(optimos[0])]


matriz = [
 [5, 8, 0, 1],
 [2, 6, 9, 4],
 [7, 0, 2, 3]
]
print(laberinto(matriz))