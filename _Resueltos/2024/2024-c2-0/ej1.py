def peso_mochila(mochila):
    peso = 0
    for elemento in mochila:
        peso += elemento[1]

def valor_mochila(mochila):
    valor = 0
    for elemento in mochila:
        valor += elemento[0]

def mochila_bt(elementos, W, k, indice, parcial, maximo):
    if len(parcial) > k:
        if peso_mochila(parcial) <= W and valor_mochila(parcial) > valor_mochila(maximo):
            maximo = parcial.copy()
        
    if indice == len(elementos):
        return maximo
    
    if peso_mochila(parcial) > W:
        return maximo

    parcial.append(elementos[indice])
    maximo = mochila_bt(elementos, W, k, indice+1, parcial, maximo)
    parcial.pop()
    maximo = mochila_bt(elementos, W, k, indice+1, parcial, maximo)

    return maximo


#elementos = (valor,peso)
def mochila(elementos,W, k):
    indice = 0
    maximo = []
    parcial = []

    mochila_bt(elementos, W, k, indice, parcial, maximo)

    return 0