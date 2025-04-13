"""
Implementar por backtracking un algoritmo que, dado un grafo no dirigido y un numero n menor a #V, devuelva si es posible obtener un subconjunto de n vertices tal que ningun par de vertices sea adyacente entre si.
"""
import grafo as g

def es_is(grafo, parcial):
    
    for w in parcial:
        for v in parcial:
            if w == v:
                continue
            if grafo.estan_unidos(v,w):
                return False
        
    return True

def IS_bt(grafo, vertices, n, indice, parcial,resultados):
    if len(parcial) == n and es_is(grafo,parcial):
        resultados = parcial[:]
        return resultados
    
    if indice >= len(vertices) or len(parcial) > n:
        return resultados
    
    if len(parcial) + len(vertices[indice:]) < n:
        return resultados

    if not es_is(grafo,parcial):
        return resultados
    

    parcial.append(vertices[indice])
    resultados = IS_bt(grafo, vertices, n, indice+1,parcial,resultados)
    parcial.pop()
    resultados = IS_bt(grafo, vertices, n, indice+1, parcial,resultados)

    return resultados


def no_adyacentes(grafo, n):
    'Devolver una lista con los n vértices, o None de no ser posible'
    vertices = grafo.obtener_vertices()

    indice = 0

    parcial = []
    resultados = []

    resultados = IS_bt(grafo,vertices, n, indice,parcial, resultados)

    if len(resultados) != n:
        return None
    return resultados


h = g.Grafo()
h.agregar_arista("A","B",1)
h.agregar_arista("A","C",1)
h.agregar_arista("B","D",1)
h.agregar_arista("B","E",1)
h.agregar_arista("C","F",1)
h.agregar_arista("E","G",1)
h.agregar_arista("F","G",1)
print(no_adyacentes(h,4))