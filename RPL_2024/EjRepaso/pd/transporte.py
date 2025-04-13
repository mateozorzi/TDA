import grafo

def modelarGrafo(tramos):
    g = grafo.Grafo(True)

    for tramo in tramos:
        origen = tramo[0]
        destino = tramo[1]
        costo = tramo[2]

        g.agregar_vertice(origen)
        g.agregar_vertice(destino)
        g.agregar_arista(origen, destino, costo)
    
    return g

def buscarOptimos(g, tramos):
    vertices = g.obtener_vertices()
    entrantes = {v: [] for v in vertices}

    #busco los entrantes
    for tramo in tramos:
        origen = tramo[0]
        destino = tramo[1]

        entrantes[destino].append(origen)

    optimos = [0] * len(vertices)

    for i in range(len(optimos)):
        #caso base -> si no tiene entrantes el costo de llegar es 0
        if len(entrantes[vertices[i]]) == 0:
            optimos[i] = 0
        
        optimos[i] = min(optimos[vertices.index(entrante)] + g.peso(entrante, vertices[i]) for entrante in entrantes[vertices[i]])
    
    return optimos, entrantes


#tramo = (A, B, costo) -> costo puede ser +costoso/-costoso
def transporte(tramos,A,B):
    g = modelarGrafo(tramos)

    optimos = buscarOptimos(g, tramos)