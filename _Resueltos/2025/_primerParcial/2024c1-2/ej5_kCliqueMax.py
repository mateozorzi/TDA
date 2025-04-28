"""
Implementar un algoritmo que dado un grafo, obtenga el clique de mayor tamaño del mismo
"""

def es_compatible(grafo, parcial, actual):
    if len(parcial) == 0:
        return True
    
    for v in parcial:
        if not grafo.estan_unidos(v, actual):
            return False
        
    return True

def k_clique_bt(grafo, vertices, indice, parcial, sol):
    if len(parcial) > len(sol):
        return parcial[:]
    
    if indice >= len(vertices):
        return sol
    
    if len(parcial) + (len(vertices) - indice) <= len(sol):
        return sol

    actual = vertices[indice]
    if es_compatible(grafo, parcial, actual):
        parcial.append(actual)
        sol = k_clique_bt(grafo, vertices, indice+1, parcial, sol)
        parcial.pop()
    sol = k_clique_bt(grafo, vertices, indice+1, parcial, sol)

    return sol

def k_clique(grafo):
    parcial = []
    sol = []

    vertices = grafo.obtener_vertices()
    indice = 0

    return k_clique_bt(grafo, vertices, indice, parcial, sol)