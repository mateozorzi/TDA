def buscarOptimos(n):
    optimos = [0] * (n + 1)
    #caso base
    optimos[0] = 0
    optimos[1] = 1

    for i in range(2, n+1):
        k = 1
        while 2*k <= i:
            optimos[i] = max( optimos[i], max(k, optimos[k]) * max(i - k, optimos[i - k]))
            k += 1
        #consigo el multiplo mas grnade que no llega a i
        #optimos[i] = max(i//2, optimos[i//2]) * max(i - i//2, optimos[i - i//2])

    return optimos
    

def reconstruccion(n, optimos, i, sol):
    if i <= 1:
        return sol
    
    k = 1
    while 2*k <= i:
        if optimos[i] == optimos[k] * optimos[i-k]:
            sol.append(k)
            return reconstruccion(n, optimos, i-k, sol)
        elif optimos[i] == k * optimos[i-k]:
            sol.append(k)
            return reconstruccion(n, optimos, i-k, sol)
        elif optimos[i] == k*k:
            sol.append(k)
            sol.append(k)
            return reconstruccion(n, optimos, 0, sol)
        k += 1
    return sol


def cortar_soga(n):
    optimos = buscarOptimos(n)

    sol = []
    sol = reconstruccion(n, optimos, len(optimos)-1, sol)
    return sol
n = 8
print(cortar_soga(n))