"""
Implementar un algoritmo que reciba un grafo no dirigido y un número k, y devuelva un ciclo de tamaño exactamente k
del grafo, si es que existe
"""
import grafo
def es_ciclo(grafo, inicial, parcial,k):
    if len(parcial) != k:
        return False
    
    if parcial[-1] == inicial and parcial[0] == inicial:
        return True
    
    return False


def ciclo_bt(grafo, vertices, visitados, inicial, actual, k, c):
    c.append(actual)
    visitados.add(actual)

    if len(c) >= k:
        return c

    if len(c) == k-1:
        if inicial in grafo.adyacentes(actual):
            c = ciclo_bt(grafo, vertices, visitados, inicial, inicial, k, c)
            return c
        else:
            c.pop()
            visitados.remove(actual)
            return c
    

    for w in grafo.adyacentes(actual):
        if w not in visitados:
            c = ciclo_bt(grafo, vertices, visitados, inicial, w, k, c)
            if es_ciclo(c, inicial, c, k):
                return c
            
    c.pop()
    visitados.remove(actual)

    return c




"""def ciclo_bt(grafo, vertices, inicial, actual, k, parcial,visitados):
    parcial.append(actual)
    visitados.add(actual)

    if len(parcial) >= k:
        return parcial
    
    if len(parcial) == k-1:
        #falta agregar un vertice, me fijo si esta el inicial
        setAdy = set(grafo.adyacentes(actual))
        if inicial in setAdy:
            parcial.append(inicial)
            return parcial

    for w in grafo.adyacentes(actual):
        if w not in visitados:
            parcial = ciclo_bt(grafo, vertices, inicial, w, k, parcial,visitados)
            if es_ciclo(grafo, inicial, parcial, k):
                return parcial
    parcial.pop()
    visitados.remove(w)"""


    #return parcial #si llego aca es que no existe ciclo de k vertices



def ciclo(grafo, k):

    vertices = grafo.obtener_vertices()
    parcial = []
    visitados = set()
    
    found = False
    for v in vertices:
        c = ciclo_bt(grafo, vertices, visitados, v, v, k, parcial)
        if len(c) == k:
            found = True
            break    
    if found:
        return c
    
    return None


g = grafo.Grafo()

# Ciclo principal de tamaño 4: B → C → D → E → B

# Aristas extra para hacer el grafo más denso
g.agregar_arista('A', 'C', 1)
g.agregar_arista('C', 'F', 1)
g.agregar_arista('F', 'D', 1)
g.agregar_arista('E', 'G', 1)
g.agregar_arista('G', 'A', 1)
g.agregar_arista('B', 'C', 1)
g.agregar_arista('C', 'D', 1)
g.agregar_arista('D', 'B', 1)
g.agregar_arista('E', 'B', 1)
g.agregar_arista('D', 'H', 1)
g.agregar_arista('H', 'I', 1)
g.agregar_arista('I', 'B', 1)

# También añadimos alguna arista “suelta”
g.agregar_arista('X', 'Y', 1)
g.agregar_arista('Y', 'Z', 1)

# Buscamos un ciclo de longitud 4
print(ciclo(g, 10))