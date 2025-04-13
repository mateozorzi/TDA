def dfs (grafo, v, visitados, padre, orden):
    visitados. agregar (v)
    for w in grafo. adyacentes (v):
        if( w not in visitados):
            padre [w] = v
            orden [w] = orden [v] + 1
            dfs (grafo, w, visitados, padre, orden)
def recorrido_dfs_completo(grafo, origen):
    visitados = set()
    padres = {}
    orden = {}
    padre [origen] = None
    orden [padre] = 0
    dfs(grafo, origen, visitados, padre, orden)
    return padre, orden

def recorrido_dfs_completo(grafo):  #si tengo mas de una comp conexa, si indico un origen puede que no visite todos lo camino del grafo
                                    #Con este ya itero con todos los vertices del grafo no visitados
    visitados = set()
    padres = {}
    orden = {}
    for v in grafo:
        if v not in visitados:
            padre [v] = None
            orden [v] = 0
            dfs (grafo, v, visitados, padre, orden)
    return padre, orden