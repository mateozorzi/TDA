
def calculoOptimos(monedas):
    optimosPepe = [[0] * (len(monedas)+1) for i in range(len(monedas)+1)]
    
    for i in range(len(optimosPepe)-1,0,-1):
        for j in range(1,len(optimosPepe)):
            if i < j:
                if j - i > 1:
                    optimosPepe[i][j] = max(
                        monedas[i-1] + max(optimosPepe[i+1][j-1], optimosPepe[i+1][j]),
                        monedas[j-1] + max(optimosPepe[i+1][j-1], optimosPepe[i][j-2])
                    )
                else:
                    optimosPepe[i][j] = max(monedas[i-1], monedas[j-1])
            if i == j:
                optimosPepe[i][j] = monedas[i-1]


    return optimosPepe
        
def inversionOptimo(monedas,optimoPepe,pos,monedasElegidas, indiceIzq, indiceDer):
    if pos == 0 or indiceDer == indiceIzq:
        return monedasElegidas
    
    if monedas[indiceDer] > monedas[indiceIzq]:
        monedasElegidas.append(indiceDer)


def monedero(monedas):
    optimoPepe = calculoOptimos(monedas)
    for i in range(len(optimoPepe)):
        print(optimoPepe[i])

    monedasElegidas = []
    return inversionOptimo(monedas, optimoPepe, len(optimoPepe)-1, monedasElegidas, 0, len(monedas)-1)


monedas = [5, 3, 7, 1, 8, 2]
print(monedero(monedas))