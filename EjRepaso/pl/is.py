import pulp
import grafo
def ind_set(grafo):
    variables = {}
    vertices = grafo.obtener_vertices()

    for v in grafo.obtener_vertices():
        variables[v] = pulp.LpVariable(f"{v}", cat="Binary")
    


    M = len(vertices)+1
    for v in vertices:
        ady = []
        for w in grafo.adyacentes(v):
            ady.append(w)
        #con esto tengo una restriccion por cada vertice
        #si variables[v] == 1, entonces la sumatoria valdra 1 y del otro lado quedara el 1
        #si variables[v] == 0, entonces la sumatoria puede tener otro valor y del otro lado quedara 1+M (que es mayor que la cantidad de vertices)
        problema += variables[v] + pulp.lpSum(variables[j] for j in ady) <= 1 + M(1-variables[v])

    problema += pulp.lpSum(variables)
    problema.solve()