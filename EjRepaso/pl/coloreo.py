import grafo
import pulp

def coloreo(grafo):
    vertices = grafo.obtener_vertices()

    variables = []
    for i in range(len(vertices)):
        variables.append(pulp.lpVariable(f"x{i}", cat="Integer", lowBound=0, upBound=len(vertices)-1))

    problema = pulp.lpProblem("Colores", pulp.lpMaximize)

    #restriccion: ningun vertice ady puede tener el mismo color
    restringidos = set()
    for v in range(len(vertices)):
        for w in range(len(grafo.adyacentes(v))):
            if vertices[v] not in restringidos and vertices[w] not in restringidos:
                problema += variables[v] - variables[w] != 0
        
        restringidos.add(vertices[v])
    #se crea una catnidad de restricciones igual a la cantidad de vertices

    problema += pulp.lpSum(variables) #funcion objetivo
    problema.solve()
