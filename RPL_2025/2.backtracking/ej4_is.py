"""
Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un máximo Independent Set del mismo.
"""
import grafo

def es_is(grafo, parcial, actual):
    
    for w in parcial:
        if grafo.estan_unidos(w, actual):
            return False   
    return True

def is_bt(grafo, vertices, indice, parcial, solucion):
    if len(parcial) > len(solucion):
        solucion = parcial[:]
    
    if indice >= len(vertices):
        return solucion
    
    if len(parcial) + len(vertices[indice:]) < len(solucion):
        return solucion
    
    if es_is(grafo, parcial, vertices[indice]):    
        parcial.append(vertices[indice])
        solucion = is_bt(grafo, vertices, indice+1, parcial, solucion)
        parcial.pop()
    solucion = is_bt(grafo, vertices, indice+1, parcial, solucion)

    return solucion

def independent_set(grafo):
    parcial = []
    solucion = []

    indice = 0

    solucion = is_bt(grafo, grafo.obtener_vertices(), indice, parcial, solucion)
    
    return solucion
