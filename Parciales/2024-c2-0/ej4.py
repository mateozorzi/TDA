import pulp

def k_clique_pl(grafo):
    vertices = grafo.obtener_vertices()
    variables = []
    #creo las variables
    for i in range(len(vertices)):
        variables.append(pulp.LpVariable(f'v{i}', cat="Binary"))
    
    #creo el problema
    problema = pulp.LpProblem("Max k_Clique", pulp.LpMaximize)

    #creo las restricciones
    #Res1: Para vertices no ady solo puede haber a lo sumo 1 en el clique maximo
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if vertices[i] == vertices[j]:
                continue
            if not grafo.estan_unidos(vertices[i], vertices[j]):
                problema += variables[i] + variables[j] <= 1
    # en el peor de los casos la cantidad de restricciones sera la cantidad de vertices * cantidad de aristas
    # esto si ningun vertice en ady con otro

    