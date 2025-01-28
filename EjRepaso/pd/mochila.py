def buscarOptimos(elementos,W):
    #filas = capacidad
    #columna = cant elementos
    optimos = [[0] * (len(elementos)+1) for _ in range(W+1)]
    
    #relleno casos base
    for i in range(len(optimos)):
        optimos[i][0] = 0
    for j in range(len(optimos[0])):
        optimos[0][j] = 0

    #ec de recurrencia: 
    #opt[i][j] = max( opt[i][j-1], opt[ i-elementos[i][1] ] [j] + elementos[i][0] )
    for i in range(1,len(optimos)):
        for j in range(1, len(optimos[i])):
            if elementos[j-1][1] > i: #no entra en la capacidad
                optimos[i][j] = optimos[i][j-1] #el optimo sera el optimo de la mochila sin este elemento
            else: #entra en la mochila con capacidad i, entonces comparo
                optimos[i][j] = max(optimos[i][j-1], optimos[i-elementos[j-1][1]][j-1] + elementos[j-1][0])
    
    return optimos
            
def reconstruccion(elementos, W, optimos, i, j, solucion):
    if i == 0 or j == 0:
        return solucion
    
    if optimos[i][j] == optimos[i][j-1]: #no use el item (j-1)
        return reconstruccion(elementos, W, optimos, i, j-1, solucion)
    else: #use el item (j-1)
        solucion.append(elementos[j-1])
        return reconstruccion(elementos,W, optimos, i-elementos[j-1][1], j-1, solucion)

#elementos = (valor, peso)
def mochila(elementos,W):
    if W == 0 or not elementos:
        return []
    optimos = buscarOptimos(elementos,W)

    #reconstruccion
    solucion = []
    solucion = reconstruccion(elementos,W,optimos, len(optimos)-1, len(optimos[0])-1, solucion)
    solucion = list(reversed(solucion))



    return solucion



arr = [(10,6), (1,1), (8,3), (100,100), (6,4), (11,2),(7,8),(2,7),(11,9)]
ganancia, solucion = mochila(arr,19)
print("Ganancia: ", ganancia)
print("Solucion: ", solucion)
"""
arr = [(10,6), (1,1), (8,3), (100,100), (6,4), (11,2),(7,8),(2,7),(11,9)]
print(mochila(arr,19))
"""