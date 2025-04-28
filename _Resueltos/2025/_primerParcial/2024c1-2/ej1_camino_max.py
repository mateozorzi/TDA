"""
Definimos a un grafo ordenado como un grafo dirigido con vértices v1, ···, vn en el que todos los vértices, salvo vn
tienen al menos una arista que sale del vértice, y cada arista va de un vértice de menor índice a uno de mayor índice (es
decir, las aristas tienen la forma (vi, vj )con i < j). Implementar un algoritmo de programación dinámica que dado
un grafo ordenado (y, si les resulta útil, una lista con los vértices en orden) determine cuál es la longitud del camino más
largo. Dar la ecuación de recurrencia correspondiente. Dar también el algoritmo de recontrucción de la solución. Indicar
y justificar la complejidad del algoritmo implementado.
"""
import grafo
def buscarOptimos(grafo):
    vertices = grafo.obtener_vertices()
    optimos = [0] * (len(vertices))

    entrantes = {v : set() for v in vertices}

    for i in range(len(vertices)):
        ady = grafo.adyacentes(vertices[i])
        for w in grafo.adyacentes(vertices[i]):
            entrantes[w].add(i)

    #Ec de recurrencia. Para el paso i, busco la cantidad maxima de vertices que me den el camino mas largo hacia i. Entonces para el vertice i, 
    # yo debere ver cual es el maximo amino para llegar a i, para esto conozco los vertices que son entrantees a este, por lo que mi optimo sera el 
    #max optimo calculado para los vetices entrantes y anteriores al vertice i
    #Ec de recu: optimos[i] = max(1 + optimos[j] for j in entrantes[v]), j < i

    for i in range(len(optimos)):
        if len(entrantes[vertices[i]]) == 0:
            optimos[i] = 0
            continue
        #si tiene entrantes
        for j in entrantes[vertices[i]]:
            optimos[i] = max(optimos[i], optimos[j] + 1 )


    return optimos, entrantes

def reconstruccion(grafo, vertices,entrantes, optimos, pos):
    sol = []
    sol.append(vertices[pos])

    while len(entrantes[vertices[pos]]) > 0:
        actual = vertices[pos]

        entrantes_actual = entrantes[vertices[pos]]

        for e in entrantes_actual:
            if optimos[e] + 1 == optimos[pos]:
                #utilice este vertice
                sol.append(vertices[e])
                pos = e
                break
    
    return sol


    


def camino_max(grafo):
    optimos, entrantes = buscarOptimos(grafo)

    return reconstruccion(grafo, grafo.obtener_vertices(),entrantes, optimos, len(optimos)-1)


g = grafo.Grafo(True)

g.agregar_arista("A", "B",1)
g.agregar_arista("C", "D",1)
g.agregar_arista("A","D",1)
g.agregar_arista("B", "D",1)
g.agregar_arista("B", "E",1)
g.agregar_arista("D", "E",1)

print(camino_max(g))
