"""
Un Vertex Cover de un Grafo G es un conjunto de vértices del grafo en el cual todas las aristas del grafo tienen al menos uno de sus extremos en dicho conjunto. Por ejemplo, el conjunto de todos los vértices del grafo siempre será un Vertex Cover.

Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un mínimo Vertex Cover del mismo.
"""
import grafo

def es_vc(grafo, vertices, parcial):
    for w in vertices:
        for v in grafo.adyacentes(w):
            if w not in parcial and v not in parcial:
                return False
            
    return True


def vc_bt(grafo, vertices, indice, parcial, sol):
    if len(sol) == 0 and es_vc(grafo, vertices, parcial):
        return parcial[:]
    
    if (len(parcial) < len(sol) and len(sol) > 0) and es_vc(grafo, vertices, parcial):
        sol = parcial[:]
        return sol
    
    if (len(parcial) > len(sol) and len(sol) > 0) or indice >= len(vertices):
        return sol
    
    

    parcial.append(vertices[indice])
    sol = vc_bt(grafo, vertices, indice+1, parcial,sol)
    parcial.pop()
    sol = vc_bt(grafo, vertices, indice+1, parcial, sol)

    return sol

def vertex_cover_min(grafo):
    parcial = []
    sol = []

    indice = 0
    vertices = grafo.obtener_vertices()
    
    sol = vc_bt(grafo, vertices, indice, parcial, sol)

    return sol

g = grafo.Grafo()

g.agregar_arista("A", "B", 1)
g.agregar_arista("A", "C", 1)
g.agregar_arista("A", "D", 1)
g.agregar_arista("B", "C", 1)
g.agregar_arista("B", "D", 1)
g.agregar_arista("C", "D", 1)

print(vertex_cover_min(g))