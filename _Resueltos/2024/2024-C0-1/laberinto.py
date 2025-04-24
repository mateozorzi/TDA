def buscarOptimos(matriz,V):
    optimos = [[0] * (len(matriz[0])+1) for _ in range(len(matriz)+1)]
    
    #caso base: la casilla (0,0) tengo la vida al maximo

    for i in range(1,len(optimos)):
        for j in range(1,len(optimos[0])):
            if i == 1 and j == 1:
                optimos[1][1] = V
            elif i == 1:
                #solo puedo ir para la izq
                optimos[i][j] = optimos[i][j-1] - matriz[i-1][j-1]
            elif j == 1:
                #solo puedo volver para arriba
                optimos[i][j] = optimos[i-1][j] - matriz[i-1][j-1]
            #ec de recurrencia, me fijo por donde me conviene venir, el optimo es el lugar donde mas vida tenga restante
            #y le resto la trampa que tenga la casilla [i][j]
            else:
                optimos[i][j] = max(optimos[i][j-1], optimos[i-1][j]) - matriz[i-1][j-1]
    
    return optimos

def reconstruccion(matriz, V, optimos, i, j, camino):
    camino.append([i-1,j-1])
    if (i,j) == (1,1):
        return camino

    if i == 1:
        #vine de la izq
        return reconstruccion(matriz, V, optimos, i, j-1, camino)
    elif j == 1:
        #vine de arriba
        return reconstruccion(matriz, V,optimos, i-1, j, camino)

    elif optimos[i][j] == optimos[i-1][j] - matriz[i-1][j-1]:
        #vine de arriba
        return reconstruccion(matriz, V, optimos, i-1, j, camino)
    elif optimos[i][j] == optimos[i][j-1] - matriz[i-1][j-1]:
        #vine de la izq
        return reconstruccion(matriz, V, optimos, i, j-1, camino)

def laberinto(matriz, V):
    optimos = buscarOptimos(matriz, V)

    camino = []
    camino = reconstruccion(matriz, V, optimos, len(optimos)-1, len(optimos[0])-1, camino)
    camino = list(reversed(camino))

    return camino, optimos[-1][-1]


n, m, V = 3, 3, 10
trampas = [
    [0, 2, 3],
    [4, 1, 5],
    [6, 2, 1]
]

print(laberinto(trampas,V))