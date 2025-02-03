def optimo(elementos, W):
    optimos = [[0 for _ in range(W+1)] for _ in range(len(elementos)+1)]

    #casos base:
    for i in range(len(optimos)):
        optimos[i][0] = 0
    for j in range(len(optimos[0])):
        optimos[0][j] = 0
    
    for i in range(len(optimos)):
        for j in range(len(optimos[0])):
            if elementos[i-1][1] > j:
                optimos[i][j] = optimos[i-1][j]
            else:
                cve = j // elementos[i-1][1] #cantidad de veces que entra en la mochila
                optimos[i][j] = max(optimos[i][j], optimos[i-1][j-(cve*elementos[i-1][1])] + elementos[i-1][0]*cve)

    return optimos

def reconstruccion(elementos, W, optimos, i, j, solucion):
    if i == 0 or j == 0:
        return solucion
    
    if optimos[i][j] == optimos[i-1][j]:
        #no use el elemento[i-1]
        return reconstruccion(elementos, W, optimos, i-1, j, solucion)
    else:
        #uso el elemento[i-1]
        cve = j // elementos[i-1][1]
        solucion.append((elementos[i-1], cve))
        return reconstruccion(elementos, W, optimos, i-1, j-(cve*elementos[i-1][1]), solucion)
    
#elemento = (valor, peso)
def mochila_repetida(elementos, W):
    optimos = optimo(elementos,W) #O(n*W)

    solucion = []
    #O(n)
    solucion = reconstruccion(elementos, W, optimos, len(optimos)-1, len(optimos[0])-1, solucion)


    return solucion

#complejidad O(n*W)