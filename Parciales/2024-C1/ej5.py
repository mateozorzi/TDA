import grafo

def calculoOptimos(vertices):
    optimos = [0] * (len(vertices)+1)
    optimos [0] = 0
    optimos[1] = vertices[0]

    for i in range(1, len(vertices)):
        optimos[i+1] = min(optimos[i-2] + vertices[i-1], optimos[i-1] + vertices[i])
        #la ec de recurrecnia, si agrego el vertrice actual, me fijo en el ioptimop anterior
        #si no agrego el actual, debo agregar el anterior, me fijo en los optimos anteriores cual da menor suma

    return optimos

def inversionOptimos(resultados, optimos,vertices,pos):
    if pos <= 0:
        return resultados
    
    if pos == 1:
        resultados.append(min(vertices[pos], vertices[pos-1]))
        return resultados

    if optimos[pos-2] + vertices[pos-1] < optimos[pos-1] + vertices[pos] and optimos[pos-2] + vertices[pos-1] < optimos[pos-1] + vertices[pos-1]:
        resultados.append(vertices[pos-1])
        return inversionOptimos(resultados, optimos, vertices, pos-2)
    elif optimos[pos-1] + vertices[pos] < optimos[pos-1] + vertices[pos-1]:
        resultados.append(vertices[pos])
        return inversionOptimos(resultados, optimos, vertices, pos-2)
    else:
        resultados.append(vertices[pos-1])
        return inversionOptimos(resultados, optimos, vertices, pos-2)
    """if pos < 0:
        return resultados
    
    if optimos[pos-1] + vertices[pos] < optimos[pos-2] + vertices[pos-1]:
        resultados.append(vertices[pos])
        return inversionOptimos(resultados,optimos,vertices, pos-2)
    return inversionOptimos(resultados,optimos,vertices,pos-1)"""
        

def DMsumaMinimaPD (grafo):
    #lit juan el vagordovich
    #ec recurrencia opt[i] = min(optimos anterior + vertice actual, optimo ant ant + vertice ante)

    vertices = grafo.obtener_vertices()
    optimos = calculoOptimos(vertices)

    resultados = []
    inversionOptimos(resultados, optimos,vertices,len(vertices)-1)
    resultados = list(reversed(resultados))

    return resultados



A = grafo.Grafo()
"""A.agregar_arista(2, 4,1)
A.agregar_arista(4, 3,1)
A.agregar_arista(3, 1,1)"""
"""A.agregar_arista(3, 2,1)
A.agregar_arista(2, 5,1)
A.agregar_arista(5, 10,1)
A.agregar_arista(10, 7,1)"""

vertices1 = [4, 1, 3, 7, 8, 2]
A.agregar_arista(4, 1,1)
A.agregar_arista(1, 3,1)
A.agregar_arista(3, 7,1)
A.agregar_arista(7, 8,1)
A.agregar_arista(8, 2,1)


print(DMsumaMinimaPD(A))