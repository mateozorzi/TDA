import heap
import grafo

def bfs(grafo, s, t):
    visitados = set()
    padres = {}
    q = heap.Heap()
    visitados.add(s)
    padres[s] = None
    q.push(s)

    while q.notEmpty():
        v = q.pop()

        if v == t:
            break

        for w in grafo.adyacentes(v):
            q.push(w)
            visitados.add(w)
            padres[w] = v
    
    if t not in visitados:
        return None
    
    camino = []
    actual = t
    while padres[actual] != None:
        camino.append(actual)
        actual = padres[actual]
    
    camino = list(reversed(camino))

    return camino

