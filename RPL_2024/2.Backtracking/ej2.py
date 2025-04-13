"""Implementar un algoritmo que reciba un grafo y un número n que, utilizando backtracking, 
indique si es posible pintar cada vértice con n colores de tal forma que no hayan dos vértices adyacentes con el mismo color."""

import grafo

def colorear(grafo, n):
    colores = {}
    vertices = grafo.obtener_vertices()
    esPosible = colorearVertices_rec(grafo,n,vertices,0,colores)
    return esPosible

def colorearVertices_rec(grafo,n,vertices,vActual,colores):
    if(vActual >= len(vertices)):
        return True   
    for c in range(n):
        colores[vertices[vActual]] = c
        if not esCompatible(grafo,colores,vertices[vActual]):
            continue
        if colorearVertices_rec(grafo,n,vertices,vActual+1,colores):
            return True
    return False

        
def esCompatible(grafo,colores,verticeActual):
    for color in colores:
        if(color == verticeActual):
            continue
        elif grafo.estan_unidos(color, verticeActual) and colores[color] == colores[verticeActual]:
                return False
    return True

if __name__ == "__main__":
    g = grafo.Grafo()
    g.agregar_arista('A', 'B', 1)
    g.agregar_arista('B', 'C', 1)
    g.agregar_arista('C', 'D', 1)
    g.agregar_arista('D', 'A', 1)

    print(colorear(g,1))