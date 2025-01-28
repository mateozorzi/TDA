def camino_minimo_bf (grafo, origen):
    dist = {}
    padre = {}
    for v in grafo:
        dist[v] = infinito
    dist[origen] = 0
    padre [origen] = None
    aristas = obtener_aristas (grafo)
    for i in range(len(grafo)):
        for v, w, peso in aristas:
            if dist[v] + peso < dist[w]:
                padre [w] = v
                dist[w] = dist[v] + peso
    for v, w, peso in aristas:
        if dist[v] + peso < dist[w]:
            return None # Hay un ciclo negativo (lanzar excep)
    return padre, dist