def camino_hamiltoniano_dfs (grafo, v, visitados, camino):
    visitados. add (v)
    camino.append (v)
    if len(visitados) == len(grafo):
        return True
    for w in grafo.adyacentes(v):
        if w not in visitados: # Esta es en sí nuestra poda
            if camino_hamiltoniano_dfs(grafo, w, visitados, camino):
                return True
    visitados. remove(v)# Permitiendo volver a venir a este vértice
    camino.pop () # por otro camino
    return False