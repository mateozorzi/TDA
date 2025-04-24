"""
Implementar un algoritmo que, por backtracking, obtenga la cantidad total de posibles ordenamientos topológicos de un grafo dirigido y acíclico.
"""
import grafo

def es_compatible(grafo, parcial, actual, grados_entradas):
    entradas_actual = grados_entradas[actual]
    
    #compruebo que esten en parcial todos lov ertices entrantes al actual
    for v in entradas_actual:
        if v not in parcial:
            return False
        
    return True
    
    
    

def contar_ordenamiento_bt(grafo, vertices, indice, grados_entradas, cant_ordenamientos, parcial):
    if len(parcial) == len(vertices):
        #no hace falta comrpibar si es comptible, porque yo solo agrego un vertice si es compatible en el paso anterior
        cant_ordenamientos += 1
        return cant_ordenamientos 
    
    if indice >= len(vertices):
        return cant_ordenamientos 
    

    if es_compatible(grafo, parcial, vertices[indice], grados_entradas) and vertices[indice] not in parcial:
        parcial.append(vertices[indice])
        cant_ordenamientos  = contar_ordenamiento_bt(grafo, vertices, 0, grados_entradas, cant_ordenamientos, parcial )
        parcial.pop()
    cant_ordenamientos = contar_ordenamiento_bt(grafo, vertices, indice+1, grados_entradas, cant_ordenamientos, parcial )

    return cant_ordenamientos 

def contar_ordenamientos(grafo):
    vertices = grafo.obtener_vertices()
    indice = 0
    grados_entradas = {v:[] for v in vertices}

    for v in vertices:
        for w in grafo.adyacentes(v):
            grados_entradas[w].append(v)
    
    cant_ordenamientos = 0

    parcial = []

    cant_ordenamientos = contar_ordenamiento_bt(grafo, vertices, indice, grados_entradas, cant_ordenamientos, parcial)

    return cant_ordenamientos


g = grafo.Grafo(True)
g.agregar_arista("A", "B",1)
g.agregar_arista("A", "C", 1)
g.agregar_arista("B", "D", 1)
g.agregar_arista("C", "E",1)
g.agregar_arista("E", "F",1)
g.agregar_arista("D", "F", 1)

print(contar_ordenamientos(g))