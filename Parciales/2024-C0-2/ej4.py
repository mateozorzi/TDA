"""
Implementar un algoritmo Greedy que busque aproximar la solución óptima al problema del mínimo Vertex Cover:
dado un grafo, obtener el mínimo Vertex Cover del mismo. Indicar la complejidad del algoritmo implementado, dar un
contraejemplo para el algoritmo implementado y justificar por qué el algoritmo implementado es un algoritmo greedy.
"""
import grafo
def vertex_cover(grafo):
    vertices = grafo.obtener_vertices()
    vertices = sorted(vertices, key=lambda x: len(grafo.adyacentes(x)), reverse=True) # complejidad O(vlogv)?

    vc = []
    cubierto = []

    for v in vertices: #O(v)
        for ady in grafo.adyacentes(v): #(E)
            if v not in cubierto and ady not in cubierto:    
                vc.append(v)
                cubierto.append(v)
    return vc
#la complejidad del algortimo sera O(cantVertices * cantAdyacentes)

#Es greedy, ya que al ordenar mis vertices por la cantidad de adyacentes
#me aseguro de siempre agregar el vertice con mas cantidad de aristas
#por lo que siempre tendre la mejor opcion para cubrir mas aristas en el momentos


A = grafo.Grafo()
A.agregar_arista(1, 2,1)
A.agregar_arista(2, 3,1)
A.agregar_arista(3,4,1)
A.agregar_arista(4,1,1)


print(vertex_cover(A))