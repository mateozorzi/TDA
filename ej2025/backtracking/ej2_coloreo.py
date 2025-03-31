"""
Implementar un algoritmo que reciba un grafo y un número n que, utilizando backtracking, indique si es posible pintar cada vértice con n colores de tal forma que no hayan dos vértices adyacentes con el mismo color.
"""
import grafo as g
def es_compatible(grafo, vertice, colores):
    for v in colores:
        if v == vertice:
            continue
        if grafo.estan_unidos(v, vertice):
            if colores[v] == colores[vertice]:
                return False
    return True

def colorear_bt(grafo, vertices, n, indice, colores):
    if len(colores) == len(vertices):
        return True    

    for color in range(n):
        colores[vertices[indice]] = color
        if es_compatible(grafo, vertices[indice], colores):
            if colorear_bt(grafo, vertices, n, indice+1, colores):
                return True
    del colores[vertices[indice]]

    return False


def colorear(grafo, n):
    colores = {}

    indice = 0

    return colorear_bt(grafo, grafo.obtener_vertices(), n, indice, colores)

h = g.Grafo()
h.agregar_arista("0","1",1)
h.agregar_arista("0","4",1)
h.agregar_arista("0","5",1)
h.agregar_arista("1","2",1)
h.agregar_arista("1","5",1)
h.agregar_arista("2","3",1)
h.agregar_arista("3","4",1)
h.agregar_arista("4","5",1)
h.agregar_arista("4","6",1)
h.agregar_arista("5","6",1)
print(colorear(h,3))