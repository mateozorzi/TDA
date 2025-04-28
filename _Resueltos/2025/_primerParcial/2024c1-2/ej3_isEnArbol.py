"""
Implementar un algoritmo greedy que permita obtener el Independent Set máximo (es decir, que contenga la mayor
cantidad de vértices) para el caso de un árbol (en el contexto de teoría de grafos, no un árbol binario). Indicar y
justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy. Indicar si el
algoritmo siempre da solución óptima. Si lo es, explicar detalladamente, sino dar un contraejemplo
"""
#regla greedy: Recorro los vertices del arbol, y voy guardando las hojas y los padres de las hojas, en cada itercacion agrego las hojas al is
#y borro los padres. De esta manera busco mazximizar la cantidad de vertice que agrego al is, agregando los hijos y salteando los padres
#Es optimos? Si, por le heho que en cada situaicon local agrego la mayor cantidad posbile ,y que haga que sea un is de vertices al conjunto, agregando
#a las hojas de mi arbol actual y luego borrando a los padres para que no sean tenido en cuenta en el proximo paso


def is_arbol(grafo):
    vertices = grafo.obtener_vertices()
    sol = []

    while len(vertices) > 0:
        vertices = grafo.obtener_vertices()
        hojas = []
        padres = set()
        for v in vertices:
            if v in padres:
                #ya se que es un padre, no lo agrego como hoja
                continue
            if len(grafo.adyacentes(v)) == 1:
                #es una hoja
                hojas.append(v)
                padres.add(grafo.adyacentes(v)[0])

        for p in padres:
            grafo.borrar_vertice(p)
        
        for h in hojas:
            sol.append(sol)
            grafo.borrar_vertice(h)

        vertices = grafo.obtener_vertices()

    return sol

#complejidad O(n^2), siendo n la cantidad de vertices del arbol
        

