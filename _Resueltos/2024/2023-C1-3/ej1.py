def buscarOptimos(grupos, W):
    #i = cant grupos
    #j = cant espacio restante
    optimos = [[0] * (W+1) for i in (len(grupos)+1)]
    
    #casos base
    #si hay 0 grupos
    for j in range(len(optimos[0])):
        optimos[0][j] = 0

    #si hay 0 espacio
    for i in range(len(optimos)):
        optimos[i][0] = 0
    

    #Ec de recurrencia:
    #si p[i] > j: el grupo entra
    #opt[i][j] = opt[i][j-1]
    # si no entra
    # opt[i][j] = max(opt[i-1][j], p[i] + opt[i-1][j-p[i-1]]) 

    for i in range(1,len(optimos)):
        for j in range(1,len(optimos[i])):
            #si entra
            if grupos[i-1] > j:
                optimos[i][j] = optimos[i-1][j]
            
            #sino entra
            optimos[i][j] = max(optimos[i-1][j], grupos[i-1] + optimos[i-1][j-grupos[i-1]])

    
    return optimos

def reconstruccion(grupos, W, optimos, i, j, solucion):
    if i == 0 or j == 0:
        return solucion
    
    if optimos[i][j] == optimos[i-1][j]:
        #no use el elemento i
        return reconstruccion(grupos, W, optimos, i-1,j, solucion)
    else:
        #uso el elemento i
        solucion.append(i-1)
        return reconstruccion(grupos, W, optimos, i-1, j-grupos[i-1], solucion)

def bodegon(grupos, W):
    optimos = buscarOptimos(grupos, W) #O(n*W)

    solucion = []

    solucion = reconstruccion(grupos, W, optimos, len(optimos)-1, len(optimos[0]), solucion ) #O(n)

    solucion = list(reversed(solucion))

    return solucion
#complejidad algoritmo O(n*W)

