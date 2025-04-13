def buscarConexiones(carteles, M):
    p = []
    for i in range(len(carteles)-1,-1,-1):
        mas_cercano = -1
        for j in range(len(carteles)-1,-1,-1):
            if i != j:
                if carteles[i][0] - carteles[j][0] >= 5: #Esta a 5km
                    mas_cercano = j
                    break
        p.append(mas_cercano)
    
    p = list(reversed(p))
    return p

def buscarOptimos(carteles, M, conexiones):
    optimos = [0] * len(carteles)+1
    for i in range(len(optimos)):
        if conexiones[i] == -1:
            optimos[i] = max(optimos[i-1], carteles[i][1])
        else:
            optimos[i] = max(optimos[i-1], carteles[i][1] + optimos[conexiones[i]])

    return optimos


def carteles(carteles, M):
    carteles = sorted(carteles, key=lambda x: x[0])
    conexiones = buscarConexiones(carteles, M)

    optimos = buscarOptimos(carteles,M, conexiones)