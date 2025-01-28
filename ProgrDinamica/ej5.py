"""Dado un laberinto representado por una grilla, 
queremos calcular la ganancia máxima que existe desde la posición (0,0) hasta la posición NxM. 
Los movimientos permitidos son, desde la esquina superior izquierda (el (0,0)), nos podemos mover hacia abajo o hacia la derecha. 
Pasar por un casillero determinado (i, j) nos da una ganancia de V_{i,j}. 
Implementar un algoritmo que, por programación dinámica, obtenga la máxima ganancia a través del laberinto. 
Hacer una reconstrucción del camino que se debe transitar. Indicar y justificar la complejidad del algoritmo implementado. 
Si hay algunos lugares por los que no podemos pasar (obstáculos), 
¿cómo se debe modificar para resolver el mismo problema?

Aclaración: solamente por simplicidad de las pruebas automáticas, devolver en este caso la ganancia máxima obtenible. Tener en cuenta que en un examen se pediría la reconstrucción de cómo se obtiene la ganancia."""

def calculoOptimos(matriz):
    optimos = [[0] * len(matriz[0]) for _ in range(len(matriz))]
    optimos[0][0] = matriz[0][0]

    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (i,j) != (0,0):
                if i == 0:
                    optimos[0][j] = matriz[0][j] + optimos[0][j-1]
                elif j == 0:
                    optimos[i][0] = matriz[i][0] + optimos[i-1][0]
                else:
                    optimos[i][j] = max(optimos[i-1][j]+matriz[i][j], optimos[i][j-1]+matriz[i][j])
                    
    return optimos

def inversionOptimo(matriz,optimos,pos,camino):
    if pos == [0,0]:
        return camino
    optimoArriba = optimos[pos[0]-1][pos[1]]+matriz[pos[0]][pos[1]]
    optimoIzq = optimos[pos[0]][pos[1]-1]+matriz[pos[0]][pos[1]]

    if (optimoArriba > optimoIzq and pos[0] > 0) or pos[1] == 0:
        camino.append((pos[0]-1,pos[1]))
        return inversionOptimo(matriz,optimos,[pos[0]-1,pos[1]],camino)
    elif (optimoArriba <= optimoIzq and pos[1] > 0) or pos[0] == 0:
        camino.append((pos[0],pos[1]-1))
        return inversionOptimo(matriz,optimos,[pos[0],pos[1]-1],camino)

def laberinto(matriz):
    if not matriz:
        return 0
    #funcion de rec -> ganancia = max(opt[i-1][j], opt[i][j-1])
    
    optimos = calculoOptimos(matriz) #O(n.m)
    camino = [( len(matriz)-1,len(matriz[0])-1 )]
    inversionOptimo(matriz,optimos,[len(matriz)-1,len(matriz[0])-1],camino)  #O(n+m)
    camino = list(reversed(camino))  #O(n+m)
    return optimos[-1][-1]
#complejidad -> n.m


matriz = [
 [5, 8, 3, 1],
 [2, 6, 9, 4],
 [7, 0, 2, 3]
]

print(laberinto(matriz))
