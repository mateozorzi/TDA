import pulp
import grafo

def vc(grafo):
    vertices = grafo.obtneer_vertices()

    variables = []
    #creo una variable por cada vertice
    for i in range(len(vertices)):
        variables.append(pulp.LpVariable('v' + str(i), cat="Binary"))
    
    problem = pulp.LpProblem("VC minimo", pulp.LpMinimize)

    #restriccion, por cada par de aristas ady al menos una debe estar en el conjunto
    for i in range(len(vertices)):
        ady = grafo.obtener_adyacentes(vertices[i])
        #la variable del vertice i + la sumatoria de sus ady debe dar al menos 1,
        #esto significa que al menos uno de los vertices esta en el conjunto
        