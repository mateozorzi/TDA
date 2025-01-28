"""Implementar un algoritmo que dado un Grafo no dirigido 
nos devuelva un conjunto de vértices que representen un máximo Independent Set del mismo."""

import grafo

def independent_set(grafo):
    vertices = grafo.obtener_vertices()
    maxIndependiente = []
    parcial = []
    maxIndependentSet(grafo,vertices,0,parcial,maxIndependiente)
    return maxIndependiente

def maxIndependentSet(grafo,vertices,actual, parcial,maxIndependiente):
    if(actual >= len(vertices)):
        if len(parcial) > len(maxIndependiente) and es_compatible(grafo, parcial):
            maxIndependiente.clear()
            maxIndependiente.extend(parcial)
        return
    
    if len(parcial) > 0:
        if not es_compatible(grafo,parcial):
            return

    
    parcial.append(vertices[actual])
    maxIndependentSet(grafo,vertices,actual+1,parcial,maxIndependiente)
    parcial.remove(vertices[actual])
    maxIndependentSet(grafo,vertices,actual+1,parcial,maxIndependiente)
    

def es_compatible(grafo,vertices):
    for v in vertices:
        for w in vertices:
            if v == w:
                continue
            if grafo.estan_unidos(v,w):
                return False
    return True

if __name__ == "__main__":
    g = grafo.Grafo()
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
    g.agregar_arista('E', 'F', 1)
    #print(g.obtener_vertices())"""
    g.agregar_vertice('A')
    g.agregar_vertice('B')
    g.agregar_vertice('C')
    g.agregar_arista('A','B',1)
    g.agregar_arista('A','C',1)


    print(independent_set(g))


"""
['A', 'B', 'C', 'D']

[]

[]

[]

[]
//////

['A', 'B', 'C', 'D']

['B', 'C', 'D']

['A']

['A']

['A']
////////////

['A', 'B', 'C', 'D']

[]

[]

[]

[]
//////////////
['A', 'B', 'C']

['B', 'C']

['A']

['A']
////////////////

['A', 'B', 'C', 'D']

['B', 'C', 'D']

['A', 'C', 'D']

['A', 'B', 'D']

['A', 'B', 'C']
/////////////////

['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

['B', 'C', 'G']

['A', 'D', 'E', 'C']

['A', 'F', 'B', 'D', 'H']

['B', 'H', 'C']

['B', 'H', 'G', 'F']

['C', 'G', 'H', 'E']

['E', 'F', 'A']

['D', 'E', 'F', 'C']
///////////////////////

['A', 'B', 'C', 'D', 'E', 'F']

['B', 'C']

['A', 'D', 'E']

['A', 'F']

['B']

['B']

['C']
///////////////////////

['A', 'B', 'C', 'D', 'E', 'F', 'G']

['B', 'C']

['A', 'D', 'E']

['A', 'F']

['B']

['B', 'G']

['C', 'G']

['E', 'F']

[]
"""