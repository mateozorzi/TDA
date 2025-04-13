"""crear un ciclo hamiltoniano, con backtracking"""
import grafo
def camino_hamiltoniano(grafo):
    visitados = []
    actual = grafo.vertice_aleatorio()
    camino = []
    vertices = grafo.obtener_vertices()

    return camino_hamiltoniano_bt(grafo,visitados,actual,camino,vertices)
    
    
def camino_hamiltoniano_bt(grafo,visitados,actual,camino,vertices):
    visitados.append(actual)
    camino.append(actual)

    
    if(len(camino) == len(vertices)):
        return camino
    
    adyacentes = grafo.adyacentes(actual)

    for a in adyacentes:
        if a not in visitados:
            camino = camino_hamiltoniano_bt(grafo,visitados,a,camino,vertices)
            return camino
    visitados.remove(actual)
    camino.remove(actual)

    return camino


if __name__ == "__main__":
    g = grafo.Grafo()
    g.agregar_arista('A', 'B', 1)
    g.agregar_arista('A', 'C', 1)
    g.agregar_arista('A', 'E', 1)
    g.agregar_arista('B', 'D', 1)
    g.agregar_arista('B', 'F', 1)
    g.agregar_arista('C', 'D', 1)
    g.agregar_arista('C', 'G', 1)
    g.agregar_arista('D', 'H', 1)
    g.agregar_arista('G', 'H', 1)
    g.agregar_arista('G', 'E', 1)
    g.agregar_arista('H', 'F', 1)
    g.agregar_arista('E', 'F', 1)
    #print(g.obtener_vertices())

    print(camino_hamiltoniano(g))