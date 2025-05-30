from collections import deque

def bfs(grafo, s, t):
    visitados = set()
    padres = {}
    cola = deque()

    visitados.append(s)
    padres[s] = None
    cola.append(s)

    while cola:
        v = cola.popleft()

        if v == t:
            break

        for ady in grafo.adyacentes(v):
            if ady not in visitados:
                cola.append(ady)
                visitados.add(ady)
                padres[ady] = v
    
    if t not in visitados:
        return None
    
    camino = []
    actual = t
    while v is not None:
        camino.append(actual)
        actual = padres[actual]

    return camino.reverse()