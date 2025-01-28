"""
Variables:
Creo una variable binaria por cada vertice del grafo (1= lo uso, 0= no lo uso)

Restricciones:
la suma de dos variables que estan unidas en el grafo, debe ser menor o igual a 1 (a lo sumo solo hay una)

Funcion Objetivo:
min de la suma de las variables


"""
import grafo
import pulp

def isPL(grafo):
    vertices = grafo.obtener_vertices()
    variables = []
    for i in range(len(vertices)):
        variables.append(pulp.LpVariable("v" + str(i), cat="Binary")) #Creo las variables

    problem = pulp.LpProblem("IS", pulp.LpMaximize)

    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if i == j:
                continue
            if grafo.estan_unidos(vertices[i], vertices[j]):
                problem += variables[i] + variables[j] <= 1 #restriccion problema
    
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
#print(grafo.obtener_vertices)
print(isPL(grafo))