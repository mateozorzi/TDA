"""
Un set dominante (Dominating Set) de un grafo G es un subconjunto D de vértices de G, tal que para todo vértice de G: o bien

(i) pertenece a D;
o bien (ii) es adyacente a un vértice en D.

Implementar un algoritmo que reciba un Grafo, y devuelva un dominating set de dicho grafo con la mínima cantidad de vértices.
"""
import grafo

def es_ds(grafo, vertices, parcial):
    for v in vertices:
        if v in parcial:
            continue
        adyacentes = grafo.adyacentes(v)
        encontrado = False
        for ady in adyacentes:
            if ady in parcial:
                encontrado = True
                continue
        if encontrado:
            continue
        return False
    
    return True

def ds_bt(grafo, vertices, indice, parcial, sol):
    if len(sol) == 0 and es_ds(grafo, vertices, parcial):
        return parcial[:]
    
    if (len(parcial) < len(sol)) and es_ds(grafo, vertices, parcial):
        return parcial[:]
    
    if (len(parcial) >= len(sol) and len(sol) > 0) or indice >= len(vertices):
        return sol


    parcial.append(vertices[indice])
    sol = ds_bt(grafo, vertices, indice+1, parcial, sol)
    parcial.pop()
    sol = ds_bt(grafo, vertices, indice+1, parcial, sol)

    return sol

def dominating_set_min(grafo):
    vertices = grafo.obtener_vertices()
    indice = 0

    parcial = []
    sol = []

    sol = ds_bt(grafo, vertices, indice, parcial, sol)
    return sol



g = grafo.Grafo()
g.agregar_arista("A", "B", 1)
g.agregar_arista("A", "C", 1)
g.agregar_arista("A", "D", 1)
g.agregar_arista("B", "C", 1)
g.agregar_arista("B", "D", 1)
g.agregar_arista("C", "D", 1)

print(dominating_set_min(g))