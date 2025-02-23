def buscarConexiones(numeros):
    p = [-1] * len(numeros)
    for i in range(len(numeros)):
        for j in range(i):
            if numeros[j] < numeros[i]:
                p[i] = j
    
    return p

def buscarOptimos(numeros, conexiones):
    optimos = [0] * len(numeros)

    #caso base: los que tienen con -1, tendran sub max = 1
    #ec recurrencia: opt[i] = max(1 + opt[p[i]], optimos[i-1])
    for i in range(len(numeros)):
        if conexiones[i] == -1:
            optimos[i] = 1
        else:
            optimos[i] = max(1 + optimos[conexiones[i]], optimos[i-1])
    
    return optimos

def reconstruccion(numeros, conexiones, optimos, i, sol):
    if conexiones[i] == -1:
        sol.append(numeros[i])
        return sol
    
    if optimos[i] == 1 + optimos[conexiones[i]]:
        sol.append(numeros[i])
        return reconstruccion(numeros, conexiones, optimos, conexiones[i], sol)
    elif optimos[i] == optimos[i-1]:
        return reconstruccion(numeros, conexiones, optimos, i-1, sol)
    


def incr_sub(numeros):
    conexiones = buscarConexiones(numeros)
    	
    optimos = buscarOptimos(numeros, conexiones)

    sol = []
    sol = reconstruccion(numeros, conexiones, optimos, len(optimos)-1, sol)
    sol = list(reversed(sol))
    return sol

num = [2,1,4,2,3,9,4,6,5,4,7]
print(incr_sub(num))
