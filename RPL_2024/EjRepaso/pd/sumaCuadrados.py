def buscarOptimos(n):
    optimos = [0] * (n + 1)
    
    #casos base
    optimos[0] = 0
    optimos[1] = 1

    for i in range(2, n+1):
        k = 1
        minimo = optimos[i-k]
        while (k*k) <= i:
            minimo = min(minimo, optimos[i-(k*k)])
            k+=1
        k-=1
        optimos[i] = min(optimos[i-1], minimo) + 1

    return optimos

def reconstruccion(n, optimos, i, sol):
    if i <= 0:
        return sol
    
    k = 1
    while (k*k) <= i:
        k+=1
        if optimos[i-1] >= optimos[i-(k*k)]:
            sol.append(k)
            return reconstruccion(n, optimos, i-(k*k), sol)


    sol.append(1)
    return reconstruccion(n, optimos, i-1, sol)
    


def suma_cuadrados(n):
    optimos = buscarOptimos(n)

    sol = []
    sol = reconstruccion(n, optimos, len(optimos)-1, sol)
    sol = list(reversed(sol))

    return sol

print(suma_cuadrados(12))