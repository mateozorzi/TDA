"""
Implementar un modelo de programación lineal que resuelva el problema de Vertex Cover mínimo (ejercicio 13 de BT)
"""

import grafo
import pulp

def vc_pl(grafo):
    
    #una varibale para cada vertice, binaria, esta en el conjunto o no
    # restriccion: para cada par de aristas debe haber uno o otro de los vertices en el conjunto
    #funcion objetivo: minimizar la cantidad de vertices en el conjunto
    vertices = grafo.obtener_vertices()
    variables = []
    for i in range(len(vertices)):
        variables.append(pulp.LpVariable(f"{vertices[i]}", cat= "Binary"))

    problema = pulp.LpProblem("VC", pulp.LpMinimize)

    #restricciones:
    for i in range(len(vertices)):
        adyacentes = []
        for j in range(len(vertices)):
            if grafo.estan_unidos(vertices[i], vertices[j]):
                problema += variables[i] + variables[j] >= 1
        
    problema += pulp.LpAffineExpression({variables[i],1} for i in range(len(variables)))
    
    problema.solve()

    return list(map(lambda yi: pulp.value(yi), variables))

g = grafo.Grafo()

g.agregar_arista("A", "B", 1)
g.agregar_arista("A", "C", 1)
g.agregar_arista("A", "D", 1)
g.agregar_arista("B", "C", 1)
g.agregar_arista("B", "D", 1)
g.agregar_arista("C", "D", 1)

print(vc_pl(g))
    