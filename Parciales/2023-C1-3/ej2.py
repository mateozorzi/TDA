def bodegon_bt(grupos, W, indice, parcial, maximo):
    if sum(parcial) > sum(maximo) and sum(parcial) <= W:
        maximo = parcial.copy()

    if indice == len(grupos):
        return maximo
    
    if sum(parcial) + sum(grupos[indice:]) < sum(maximo):
        return maximo

    parcial.append(grupos[indice])
    maximo = bodegon_bt(grupos, W, indice+1, parcial, maximo)
    parcial.pop()
    maximo = bodegon_bt(grupos,W, indice+1, parcial, maximo)

    return maximo

def bodegon(grupos, W):
    maximo = []
    parcial = []
    indice = 0

    maximo = bodegon_bt(grupos,W, indice, parcial, maximo)
    return maximo