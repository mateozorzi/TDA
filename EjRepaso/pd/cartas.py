
def buscarOptimos(mazo):
    optimos = [[0 for _ in range(len(mazo[0]))] for __ in range(len(mazo))]

    #ec de recurrencia:
    # i > j -> opt[i][j] = 0
    # i = j -> opt[i][j] = mazo [i]
    # j - i == 2 -> opt[i][j] = max(mazo[i], mazo[j])
    #else:
        # opt[i][j] == -> max(
        #                       mazo[i] + max(opt[i+2][j], opt[i+1][j-1]),
        #                       mazo[j] + max(opt[i+1][j-1], opt[i][j-2])  

    for i in range(len(mazo),-1,-1):
        for j in range(len(mazo),-1,-1):
            if i > j:
                optimos[i][j] = 0
            elif i == j:
                optimos[i][j] = mazo[i]
            elif j - i == 2:
                optimos[i][j] = max(mazo[i], mazo[j])
            else:
                optimos[i][j] = max(
                    mazo[i] + max(optimos[i+2][j], optimos[i+1][j-1]),
                    mazo[j] + max(optimos[i][j-2], optimos[i+1][j-1])
                )      

    return optimos


def cartas(mazo):
    optimos = buscarOptimos(mazo)