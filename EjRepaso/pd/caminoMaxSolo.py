import grafo
def buscarOptimos(grafo, vertices):
    entrantes = {v: [] for v in vertices}
    for i in range(len(vertices)):
        for w in grafo.adyacentes(vertices[i]):
            entrantes[w].append(i)

    #caso base, los vertices que no les entran aristas tienen camino = 0
    optimos = [0] * len(vertices)
    for i in range(len(vertices)):
        if len(entrantes[vertices[i]] )== 0:
            optimos[i] = 0
            continue
        #si tienen al menos una arista, busco el camino maximo con el que se puede llegar
        optimos[i] = max(optimos[k] for k in entrantes[vertices[i]]) + 1
        
            
    
    return optimos, entrantes

def reconstruccion(grafo, vertices, optimos, i,entrantes, sol):
    sol.append(vertices[i])
    if len(entrantes[vertices[i]]) == 0:
        return sol
    
    for k in entrantes[vertices[i]]:
        if optimos[k] + 1 == optimos[i]:
            return reconstruccion(grafo, vertices, optimos, k, entrantes, sol)
    

def camino_max(grafo):
    vertices = grafo.obtener_vertices()

    optimos, entrantes = buscarOptimos(grafo, vertices)

    sol = []
    sol = reconstruccion(grafo, vertices, optimos, len(optimos)-1,entrantes, sol)
    return sol

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
g.agregar_arista(4,5)

camino_max(g)