import pulp
import grafo

#busco minimizar la funcion objetivo
#variables -> una por vertice, binarias, 1 que uso el vertice, 0 que no
#Restricciones, cara cada arista v1-v2, debe estar en el conjunto al menos uno de los dos vertices
#funcion objetivo, sera la sumatoria de los vertices, buscare el minimo posible
def vertex_cover_min(grafo):
    vertices = grafo.obtener_vertices()
    variables = []

    for i in range(len(vertices)):
        variables.append(pulp.LpVariable('v' + str(i), cat="Binary"))

    problem = pulp.LpProblem("VC minimo", pulp.LpMinimize)

    #restricciones
    for i in range(len(vertices)):
        for w in range(len(vertices)):
            if vertices[i] == vertices[w]:
                continue
            if grafo.estan_unidos(vertices[i], vertices[w]):
                problem += variables[i] + variables[w] >= 1

    problem += pulp.LpAffineExpression([{variables[i], 1} for i in range(len(variables))])
    problem.solve()

    return list(map(lambda vi: pulp.value(vi), variables))

grafo = grafo.Grafo()
grafo.agregar_arista('A','B',1)
grafo.agregar_arista('A','D',1)
grafo.agregar_arista('B','C',1)
grafo.agregar_arista('C','D',1)
grafo.agregar_arista('C','E',1)
grafo.agregar_arista('E','D',1)

print(vertex_cover_min(grafo))