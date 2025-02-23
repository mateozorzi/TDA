def buscarOptimos(paquetes, P):
    optimos = [[0] for _ in range(P+1) for _ in range(len(paquetes)+1)]

    #caso base, si no tengo paquetes el optimo es cero o si no tengo espacio el optimo es cero
    for i in range(len(optimos)):
        optimos[i][0] = 0
    for j in range(len(optimos[0])):
        optimos[0][j] = 0
    
    #ec de recurrencia:
    #Opt[i][j] -> paq[i][1] > 0 and paq[i][0] <= j -> cant = j//paq[i][0] si la cantidad es menor al inventario, coloco eta cantidad, si es mayor coloco todo el inventario
    #          -> else: opt[i][j] = opt[i-1][j] no cuento este elemento

    for i in range(1,len(optimos)):
        for j in range(1, len(optimos[0])):
            if paquetes[i][1] > 0 and paquetes[i][0] <= j:
                #entra en el pedido
                cant = j//paquetes[i][0]
                
                if cant > paquetes[i][1]:
                    cant = paquetes[i][1]
                
                optimos[i][j] = optimos[i-1][j-cant*paquetes[i][0]] + cant
            else:
                optimos[i][j] = optimos[i-1][j]
    return optimos



#Paquetes: (tamaño, restantes)
#P = tamaño pedido
def inventarioEmpaques(paquetes, P):
    optimo = buscarOptimos(paquetes, P)