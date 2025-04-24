def buscarOptimos(grafo, vertices, origen, destino):
    optimos = [0] * len(vertices)

    #busco las entradas a los vertices
    entradas = {v: [] for v in vertices}
    for i in range(len(vertices)):
        for w in grafo.adyacentes(vertices[i]):
            entradas[w].append(i)
    
    #casos base -> el oprigen no tiene entradas por lo que el optimo es cero
    optimos[origen] = 0

    #calculo los optimos
    for i in range(len(optimos)):
        if vertices[i] == origen:
            continue
        vertice_actual = vertices[i]
        entradas_actual = entradas[vertice_actual]
        optimos[i] = max(grafo.peso_arista(vertices[entradas_actual[j]], vertice_actual) + optimos[entradas_actual[j]] for j in range(len(entradas_actual)))
    
    return optimos, entradas
            
def reconstruccion(grafo, vertices, origen, destino, optimos, i, entradas, sol):
    sol.append(vertices[i])
    if vertices[i] == origen:
        return sol
    
    for v in entradas[vertices[i]]:
        if optimos[i] == grafo.peso_arista(vertices[v], vertices[i]) + optimos[v]:
            return reconstruccion(grafo, vertices, origen, destino, optimos, v, entradas, sol)

def camino_max(grafo, s, t):
    vertices = grafo.obtener_vertices()
    optimos, entradas = buscarOptimos(grafo, vertices, s, t)

    sol = []
    sol = reconstruccion(grafo, vertices, s, t, optimos, len(optimos)-1,entradas, sol)
    sol = list(reversed(sol))

    return sol