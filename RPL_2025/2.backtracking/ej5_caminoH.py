"""
Un camino hamiltoniano, es un camino de un grafo, que visita todos los vértices del grafo una sola vez. Implementar un algoritmo por backtracking que encuentre un camino hamiltoniano de un grafo dado.
"""

def caminoH_bt(grafo, vertice, visitados, camino):

    camino.append(vertice)
    visitados.add(vertice)

    if len(visitados) == len(grafo.obtener_vertices()):
        return camino
    
    for w in grafo.adyacentes(vertice):
        if w not in visitados:
            camino = caminoH_bt(grafo, w, visitados, camino)
            if len(camino) == len(grafo.obtener_vertices()):
                return camino
    
    camino.pop()
    visitados.remove(vertice)
        
        
    return camino #devuelvo el camino aunque no haya ebncontrado, para poder ir eliminando los vertices que fui vistando

def camino_hamiltoniano(grafo):
    visitados = set()
    camino = []

    for v in grafo.obtener_vertices():
        camino = caminoH_bt(grafo, v, visitados, camino)
        if len(camino) == len(grafo.obtener_vertices()):
            return camino
    
    return []