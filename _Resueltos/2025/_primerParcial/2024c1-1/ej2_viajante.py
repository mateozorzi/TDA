"""
Implementar un algoritmo greedy que permita obtener el mínimo del problema del viajante: dado un Grafo pesado G y
un vértice de inicio v, obtener el camino de menor costo que lleve a un viajante desde v hacia cada uno de los vértices
del grafo, pasando por cada uno de ellos una única vez, y volviendo nuevamente al origen. Se puede asumir que el grafo
es completo. Indicar y justificar la complejidad del algoritmo implementado.
¿El algoritmo obtiene siempre la solución óptima? Si es así, justificar detalladamente, sino dar un contraejemplo. Indicar
y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy
"""
import grafo
def viajante(grafo, v):
    padres = {}
    pesos = {w: 0 for w in grafo.obtener_vertices()} #peso de llegar desde v a w
    visitados = set()
    padres[v] = None
    visitados.add(v)
    vertices = grafo.obtener_vertices()

    actual = v
    while len(visitados) < len(vertices):
        
        min = 0
        sig = None
        for k in grafo.adyacentes(actual):
            if k in visitados:
                continue
            peso_arista = grafo.peso_arista(actual, k)
            if min == 0 or peso_arista < min:
                min = peso_arista
                sig = k
        
        padres[sig] = actual
        pesos[sig] += min + pesos[actual]
        visitados.add(sig)
        actual = sig

    peso_arista = grafo.peso_arista(actual, v)
    pesos[v] += peso_arista + pesos[actual]

    return pesos
#regla greedy: en mi situacion local estoy parado en un vertice, para moverme la siguiente vertice me movere por la arista de menor peso entre los ady no visitados de mi vertice actual
#de esta manera busco siempre dar el paso que menos costo me sume en mi situacion local
#Es optimo? 
#no lo es:
#  A -> 9 -> B -> 10000 -> C
#    -> 10 -> D -> 1 -> C -> 1 -> B -> 1 -> A
#le algortimo enocntraria el camino que primero va de A -> B porque es la arista de menor peso actual, pero luego tendria que pasar por C que tiene un peso mucho mayor.
#Un camino optimo deberia haber sido A -> D -> C -> B -> A que suma 13

g = grafo.Grafo(True)

g.agregar_arista("A", "B", 1)
g.agregar_arista("A", "D", 10)
g.agregar_arista("D", "C", 1)
g.agregar_arista("C", "B", 1)
g.agregar_arista("B", "C", 100000)
g.agregar_arista("C", "D", 1)
g.agregar_arista("B", "A", 1)
g.agregar_arista("D", "A", 1)

print(viajante(g, "A"))


