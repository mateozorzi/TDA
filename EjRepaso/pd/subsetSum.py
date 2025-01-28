def buscarOptimos(elementos, v):
    optimos = [[0] * (v+1) for _ in range(len(elementos)+1)]

    for i in range(1, len(optimos)):
        for j in range(1, len(optimos[i])):
            if elementos[i-1] > j: #el valor se pasa del numero a sumar, entonces me quedo con el otpimos anterior
                optimos[i][j] = optimos[i-1][j]
            else: #el valor entra en el numero a sumar
                optimos[i][j] = max(optimos[i-1][j], optimos[i-1][j-elementos[i-1]] + elementos[i-1])

    return optimos

def reconstruirSolucion(elementos, v, optimos, i, j, solucion):
    if i == 0 or j == 0:
        return solucion
    
    if optimos[i][j] == optimos[i-1][j]: #No use el numero en la suma
        return reconstruirSolucion(elementos, v, optimos, i-1, j, solucion)
    else: #uso el numero en la suma
        solucion.append(elementos[i-1])
        return reconstruirSolucion(elementos, v, optimos, i-1, j-elementos[i-1], solucion)

def subset_sum(elementos, v):
    if not elementos or v == 0:
        return []
    optimos = buscarOptimos(elementos, v)

    solucion = []
    solucion = reconstruirSolucion(elementos, v, optimos, len(optimos)-1, len(optimos[0])-1, solucion)
    solucion = list(reversed(solucion))

    return solucion

elementos = [3, 34, 4, 12, 5, 2]
v = 9
print(subset_sum(elementos, v)) # [4, 5]