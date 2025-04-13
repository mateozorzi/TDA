import pulp
import grafo

def clique_max(grafo):
    vertices = grafo.obtener_vertices()

    variables_vertices = {}
    for v in vertices:
        variables_vertices[v] = pulp.LpVariable(f"{v}", cat="Binary")
    
    c_max = pulp.lpVariable('c_max', cat="Integer", lowBound=0, upBound=len(vertices))

    problema = pulp.LpProblem("Clique maximo", pulp.LpMaximize)


    #restriccion: como hago para que se forme un subgrafo completo
    M = len(vertices) + 1
    for v in vertices:
        ady = []
        for w in grafo.adyacentes(v):
            ady.append(w)
        problema += variables_vertices[v] + pulp.lpSum([variables_vertices[w] for w in ady]) >= c_max - M(1 - variables_vertices[v])

    problema += c_max
    problema.solve()