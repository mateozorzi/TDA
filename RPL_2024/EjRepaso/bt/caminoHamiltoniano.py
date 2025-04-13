import grafo

def camino_hamiltoniano_bt(grafo, vertice, camino, visitados, caminoHamiltoniano):
    visitados.append(vertice)
    camino.append(vertice)
    if len(visitados) == len(grafo.obtener_vertices()):
        return camino
    for w in grafo.adyacentes(vertice):
        if w not in visitados: # Esta es en sí nuestra poda
            camino_hamiltoniano_bt(grafo, w, camino, visitados, caminoHamiltoniano)
            if len(visitados) == len(grafo.obtener_vertices()):
                return camino
    visitados.remove(vertice)# Permitiendo volver a venir a este vértice
    camino.pop() # por otro camino
    return None


#agrego al camino
#pruebo esta "rama" de solucion
#quito del camino
#pruebo otra solucion sin este vertice

def camino_hamiltoniano(grafo):
    vertices = grafo.obtener_vertices()

    visitados = []

    camino = []

    caminoHamiltoniano = []

    for v in vertices:
        if camino_hamiltoniano_bt(grafo, v, camino, visitados, caminoHamiltoniano):
            return camino
    return None

#no dirigido
"""g = grafo.Grafo()
g.agregar_arista('0','2',1)
g.agregar_arista('0','4',1)
g.agregar_arista('0','5',1)
g.agregar_arista('1','4',1)
g.agregar_arista('1','5',1)
g.agregar_arista('2','4',1)
g.agregar_arista('2','3',1)
g.agregar_arista('4','5',1)"""

#dirigido
g = grafo.Grafo()
g.agregar_arista('0','2',1)
g.agregar_arista('0','4',1)
g.agregar_arista('0','5',1)
g.agregar_arista('1','4',1)
g.agregar_arista('1','5',1)
g.agregar_arista('2','0',1)
g.agregar_arista('2','4',1)
g.agregar_arista('3','4',1)
g.agregar_arista('4','0',1)
g.agregar_arista('4','1',1)
g.agregar_arista('4','2',1)
g.agregar_arista('4','3',1)
g.agregar_arista('4','5',1)
g.agregar_arista('5','0',1)
g.agregar_arista('5','1',1)
g.agregar_arista('5','4',1)



"""g.agregar_arista('A', 'B', 1)
g.agregar_arista('A', 'C', 1)
g.agregar_arista('A', 'E', 1)
g.agregar_arista('B', 'D', 1)
g.agregar_arista('B', 'F', 1)
g.agregar_arista('C', 'D', 1)
g.agregar_arista('C', 'G', 1)
g.agregar_arista('D', 'H', 1)
g.agregar_arista('G', 'H', 1)
g.agregar_arista('G', 'E', 1)
g.agregar_arista('H', 'F', 1)
g.agregar_arista('E', 'F', 1)"""
#print(g.obtener_vertices())

print(camino_hamiltoniano(g))