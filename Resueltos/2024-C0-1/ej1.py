
def calculoOptimo(matriz,n,m,vida):
    optimos = [[0] * (n+1) for i in range(m+1)]

    for i in range(1,len(optimos)):
        for j in range(1,len(optimos)):
            if i == 1 and j == 1:
                optimos[i][j] = vida
            elif i == 1:
                optimos[i][j] = optimos[i][j-1] - matriz[i-1][j-1]
            elif j == 1:
                optimos[i][j] = optimos[i-1][j] - matriz[i-1][j-1]
            else:
                optimos[i][j] = max(optimos[i][j-1], optimos[i-1][j]) - matriz[i-1][j-1]

    return optimos    

def inversionOptimo(optimos, pos, camino):
    if pos[0] == 0 or pos[1] == 0 or pos == [1,1]:
        return camino

    if optimos[pos[0]][pos[1]-1] > optimos[pos[0]-1][pos[1]]:
        camino.append([pos[0]-1, pos[1]-2])
        return inversionOptimo(optimos, [pos[0], pos[1]-1], camino)
    else:
        camino.append([pos[0]-2,pos[1]-1])
        return inversionOptimo(optimos, [pos[0]-1, pos[1]], camino)

def laberinto(matriz,n,m,vida):
    caminoOptimo = calculoOptimo(matriz,n,m,vida) #O(n x m), espacio de (n+1 x m+1) polinomial
    camino = [[len(caminoOptimo)-2, len(caminoOptimo[0])-2]] 
    inversionOptimo(caminoOptimo, [len(caminoOptimo)-1, len(caminoOptimo[0])-1],camino) #O(n)
    camino = list(reversed(camino)) #O(n), espacio polinomial

    return camino

n, m, V = 3, 3, 10
trampas = [
    [0, 2, 3],
    [4, 1, 5],
    [6, 2, 1]
]

print(laberinto(trampas,n,m,V))