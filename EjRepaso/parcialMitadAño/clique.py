import grafo

def esClique(grafo, subgrafo):
    cant_vertices = len(subgrafo)
    for v in subgrafo:
        if len(subgrafo.adyacentes(v)) != cant_vertices - 1:
            return False
    
    return True

def clique_bt(grafo, vertices, indice, subgrafoMaximo, parcial):
    if len(subgrafoMaximo) < len(parcial) and esClique(grafo, parcial):
        subgrafoMaximo = parcial.copy()
    
    if indice == len(vertices):
        return subgrafoMaximo

    if len(subgrafoMaximo) > len(parcial) + len(vertices[indice:]):
        return subgrafoMaximo #con los vertices restantes no llego al subgrafo maximo

    parcial.append(vertices[indice])
    subgrafoMaximo = clique_bt(grafo, vertices, indice+1, subgrafoMaximo, parcial)
    parcial.pop()
    subgrafoMaximo = clique_bt(grafo, vertices, indice+1, subgrafoMaximo, parcial)

    return subgrafoMaximo

def clique(grafo):
    vertices = grafo.obtener_vertices()
    indice = 0

    subgrafoMaximo = []
    parcial = []

    subgrafoMaximo = clique_bt(grafo, vertices, indice, subgrafoMaximo, parcial)

    return subgrafoMaximo

g = grafo.Grafo()
g.agregar_vertice("A")
g.agregar_vertice("B")
g.agregar_vertice("C")
g.agregar_vertice("D")
g.agregar_vertice("E")
g.agregar_vertice("F")
g.agregar_vertice("G")

g.agregar_arista("A", "B",1)
g.agregar_arista("A", "C",1)
g.agregar_arista("A", "D",1)
g.agregar_arista("A", "E",1)
g.agregar_arista("B", "C",1)
g.agregar_arista("B", "D",1)
g.agregar_arista("B", "E",1)
g.agregar_arista("C", "D",1)
g.agregar_arista("C", "E",1)
g.agregar_arista("D", "E",1)
g.agregar_arista("A", "F",1)
g.agregar_arista("B", "F",1)
g.agregar_arista("B", "G",1)

print(clique(g)) #['A', 'B', 'C', 'D', 'E']

    