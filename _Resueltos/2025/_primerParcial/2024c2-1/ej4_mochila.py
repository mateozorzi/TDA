"""
Implementar un algoritmo que, por programación dinámica, resuelva el problema de la mochila con una variante:
ahora se puede poner una cantidad ilimitada de un mismo elemento (es decir, se puede repetir), siempre y cuando
aún haya lugar. Por ejemplo, si yo tengo un elemento de tamaño 3 y una mochila de tamaño 10, yo podría guardar
3 veces dicho elemento, si así lo quisiera (también menos cantidad). Escribir y describir la ecuación de recurrencia
de la solución, y la complejidad del algoritmo implementado. Implementar o explicar (la que prefieran) cómo sería el
algoritmo de reconstrucción de la solución, indicando su complejidad
"""

def buscarOptimos(elementos, W):
    optimos = [[0] * (W+1) for _ in range(len(elementos)+1)]

    #ec de recurrencia, sera parecido al de la mochila solo con el agregado de la logica que poder agregar mas de una vez ele lemento si entra en la capacidad
    # si tengo un elemento que netra en la mochila tengo dos opciones   -> No lo uso
    #                                                                   -> lo uso
    #si uso el elemento, puedo ver cuantas veces entra en la mochila W // peso_elemento,
    #para saber cual es el optimo para la mochila de capacidad j y cant de elemtnos i, tengo
    # opt[i][j] = max(  optimos[i-1][j]     ,    optimos[i-1][j-cant*peso_elemento] + cant*valor_elemento          )
    #                   sin usar el elemento,       usando el elemento comko optimo

    for i in range(1, len(optimos)):
        for j in range(1, len(optimos[0])):
            elemento_actual = elementos[i-1]
            peso_elemento = elemento_actual[1]
            valor_elemento = elemento_actual[0]

            if peso_elemento > j:
                optimos[i][j] = optimos[i-1][j]
                continue

            cant = j // peso_elemento
            optimos[i][j] = max(optimos[i-1][j], optimos[i-1][j-(cant*peso_elemento)] + (cant*valor_elemento))

    return optimos

def reconstruccion(elementos, W, optimos, i, j):
    sol = []

    while i > 0 and j > 0:

        optimos_anterior = optimos[i-1][j]

        elemento_actual = elementos[i-1]
        peso_elemento = elemento_actual[1]
        valor_elemento = elemento_actual[0]

        if j >= peso_elemento:
            cant = j // peso_elemento
            optimo_con_elemento = optimos[i-1][j - (cant*peso_elemento)] + (cant*valor_elemento)
            if optimo_con_elemento >= optimos_anterior:
                sol.append(elemento_actual)
                i -= 1
                j -= (cant*peso_elemento)
            else:
                i -= 1
        else:
            i -= 1

    return sol



#elemento = (valor, peso)
def mochila_repetida(elementos, W):
    optimos = buscarOptimos(elementos, W)

    sol = reconstruccion(elementos, W, optimos, len(optimos)-1, len(optimos[0])-1)
    return sol