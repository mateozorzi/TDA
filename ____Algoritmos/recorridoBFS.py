import heapq

def bfs (grafo, origen):
    visitados = set()
    padres = {}
    orden = {}
    q = heapq.Heap()
    visitados.agregar(origen)
    padres [origen] = None
    orden[origen] = 0
    q. encolar(origen)
    while not q. esta_vacia():
        v = q. desencolar ()
        for w in grafo. adyacentes(v):
            if( w not in visitados):
                visitados.agregar (w)
                padres [w] = v
                orden [w] = orden [v] + 1
                q. encolar (w)
    return padres, orden

def camino(grafo, s, t):
    visitados = set()
    padres = {}
    orden = {}
    q = heapq.Heap()
    visitados.agregar(s)
    padres [s] = None
    orden[s] = 0
    q. encolar(s)
    while not q. esta_vacia():
        v = q. desencolar ()

        if v == t: #Encontre el destino
            break

        for w in grafo. adyacentes(v):
            if( w not in visitados):
                visitados.agregar (w)
                padres [w] = v
                orden [w] = orden [v] + 1
                q. encolar (w)

    if t not in visitados:
        return None
    
    camino = []
    vertice = t
    while vertice is not None:
        camino.append(vertice)
        vertice = padres[vertice]
    
    camino.reverse()

    return camino  