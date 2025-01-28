"""Implementar un algoritmo que dado un Grafo no dirigido nos devuelva 
un conjunto de vértices que representen un mínimo Vertex Cover del mismo."""
import grafo

def vertex_cover_min(grafo):
    minimo = []
    vertex_cover = []
    vertices = grafo.obtener_vertices()
    if(len(vertices) == 0):
        return []
    indice = 0    
    minimo = vertex_cover_min_bt(grafo, vertices,indice, minimo,vertex_cover)

    return minimo

def estaCubierto(grafo,vertex_cover):
    for v in grafo.obtener_vertices():
        if v not in vertex_cover:
            if not any(grafo.estan_unidos(v,w) for w in vertex_cover):
                return False
        
        for w in grafo.adyacentes(v):
            if v not in vertex_cover and w not in vertex_cover:
                return False


    return True

def vertex_cover_min_bt(grafo, vertices,indice, minimo,vertex_cover):
    if(len(vertex_cover) == len(vertices)):
        return
    
    if(len(vertex_cover) < len(minimo) or len(minimo) == 0) and (len(vertex_cover) > 0):
        if(estaCubierto(grafo,vertex_cover)):
            minimo[:] = vertex_cover[:]

    if(indice >= len(vertices)):
        return
    vertex_cover.append(vertices[indice])
    vertex_cover_min_bt(grafo,vertices,indice+1,minimo,vertex_cover)
    vertex_cover.pop()
    vertex_cover_min_bt(grafo,vertices,indice+1,minimo,vertex_cover)
    
    
    return minimo



grafo = grafo.Grafo()
grafo.agregar_arista('A','B',1)
grafo.agregar_arista('A','D',1)
grafo.agregar_arista('B','C',1)
grafo.agregar_arista('C','D',1)
grafo.agregar_arista('C','E',1)
grafo.agregar_arista('E','D',1)

print(vertex_cover_min(grafo))