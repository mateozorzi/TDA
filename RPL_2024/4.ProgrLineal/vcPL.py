"""
Variables:
Una variable por cada vertice del grafo, sera binaria   -> 1 la uso en el vertex cover
                                                        -> 0 no la uso

Ecuaciones e inecuaciones:
la sumatoria de dos vertices adyacentes debe ser mayor  o igual que 1 (que por lo menos uno este)
para todo par de vertices, la suma de las variable sdebe ser mayor  o igual que 1

Funcion Objetivo:
min de la sumatoria de las variables
"""
import grafo
import pulp

def vcPL(grafo):
    v = []
    vertices = grafo.obtener_vertices()
    for i in range(len(vertices)):
        v.append(pulp.LpVariable("v" + str(i), cat="Binary")) #creo las variables binarias
    problem = pulp.LpProblem("Vertex Cover", pulp.LpMinimize)
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if i == j:
                continue
            if grafo.estan_unidos(vertices[i],vertices[j]):
                problem += v[i] + v[j] >= 1 #Que una de las dos sea 1 o las dos
    problem += pulp.LpAffineExpression([{v[i], 1} for i in range(len(v))])

    problem.solve()
    return list(map(lambda vi: pulp.value(vi), v))



grafo = grafo.Grafo()
grafo.agregar_arista('A','B',1)
grafo.agregar_arista('A','D',1)
grafo.agregar_arista('B','C',1)
grafo.agregar_arista('C','D',1)
grafo.agregar_arista('C','E',1)
grafo.agregar_arista('E','D',1)

print(vcPL(grafo))