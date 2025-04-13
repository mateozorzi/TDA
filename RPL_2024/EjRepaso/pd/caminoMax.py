import grafo

def buscarOptimos(grafo, vertices, vertices_entrantes):
    #optimos = [0] * (len(vertices)+1)
    optimos = {v : 0 for v in vertices}

    #Ec de recurrencia
    #opt[i] = 1 + max(opt[j]) para j un vertice entrante a i
    for i in range(len(optimos)):
        if len(vertices_entrantes[i+1]) == 0:
            optimos[i] = 0
        else:    
            optimos[i] = 1 + max([optimos[j] for j in vertices_entrantes[i+1]])

    return optimos

"""def reconstruirCamino(grafo, optimos, vertices, vertices_entrantes, pos, camino):
    if pos <= 0:
        return camino
    
    for v in vertices_entrantes[pos]:
        if optimos[pos] - 1 == """

def caminoMax(grafo):
    vertices = grafo.obtener_vertices()
    
    vertices_entrantes = {v: set() for v in vertices}
    for v in vertices:
        for w in grafo.adyacentes(v):
            vertices_entrantes[w].add(v)
    
    optimos = buscarOptimos(grafo, vertices, vertices_entrantes)


g = grafo.Grafo(True)
g.agregar_vertice(1)
g.agregar_vertice(2)
g.agregar_vertice(3)
g.agregar_vertice(4)
g.agregar_vertice(5)

g.agregar_arista(1,2)
g.agregar_arista(1,4)
g.agregar_arista(2,4)
g.agregar_arista(2,5)
g.agregar_arista(3,4)
g.agregar_arista(3,5)
g.agregar_arista(4,5)

print(caminoMax(g))