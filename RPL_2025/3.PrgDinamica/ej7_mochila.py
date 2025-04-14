"""Tenemos una mochila con una capacidad W. Hay elementos a guardar, 
cada uno tiene un valor, y un peso que ocupa de la capacidad total. 
Queremos maximizar el valor de lo que llevamos sin exceder la capacidad. 
Implementar un algoritmo que, por programación dinámica, 
reciba los valores y pesos de los elementos, 
y devuelva qué elementos deben ser guardados para maximizar la ganancia total. 
Indicar y justificar la complejidad del algoritmo implementado."""

def buscarOptimos(elementos, W):
    optimos = [[0] * (W+1) for _ in range(len(elementos)+1)]
    #fil -> cant elementos
    #col -> capacidad restante

    #Ec de recurrencia -> opt[i][j] = max(      opt[i-1][j],              opt[i-1][j - pesoElemento[i]] + ganancia[i])
    #                                       no uso el elemento                          uso el elemento, ahora tengo 
    #                                                                                   una mochila con menos capacidad
    #caso base  -> cant elementos = 0 -> opt[0][j] = 0
    #           -> capacidad = 0 -> opt[i][0] = 0
    for i in range(1,len(optimos)):
        for j in range(1,len(optimos[0])):
            elementoActual = elementos[i-1]
            peso = elementoActual[0]
            valor = elementoActual[1]

            #si el peso es mayor a la capacidad restante, me salteo este objeto
            if peso > j:
                optimos[i][j] = optimos[i-1][j]
            
            #sino comparo, entre el optimo sin contar este elemento y con la misma capacidad, o pongo el elemento y veo cual es el optimo con la capacidad reducida
            optimos[i][j] = max(optimos[i-1][j], optimos[i-1][j - peso] + valor)

    return optimos

def reconstruccion(elementos, W, optimos, i,j):
    sol = []

    while i > 0 and j > 0:
        actual = optimos[i][j]

        sinElemento = optimos[i-1][j]
        conElemento = optimos[i-1][j - elementos[i-1][0]]

        if sinElemento == actual:
            #no use el elemento (i-1)
            i -= 1
        elif conElemento + elementos[i-1][1] == actual:
            #uso el elemento
            i -= 1
            j -= elementos[i-1][0] #resto capacidad restante de la mochila
            sol.append(elementos[i-1])
        
    return sol

def mochila(elementos, W):
    optimos = buscarOptimos(elementos, W)

    sol = reconstruccion(elementos, W, optimos, len(optimos)-1, len(optimos[0])-1)

    return sol
