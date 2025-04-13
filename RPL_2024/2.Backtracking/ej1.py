"""Implementar por backtracking un algoritmo que, dado un grafo no dirigido y un numero n menor a #V, 
devuelva si es posible obtener un subconjunto de n vertices tal que ningun par de vertices sea adyacente entre si."""
import grafo as Grafo

def no_adyacentes(grafo, n):
    'Devolver una lista con los n vértices, o None de no ser posible'
    verticesNoAdyacentes = []
    vertices = grafo.obtener_vertices()
    if(n > len(vertices)):
        return None
    verticesNoAdyacentes = no_adyacentes_rec(grafo,n,vertices, 0,verticesNoAdyacentes)
    return verticesNoAdyacentes

def no_adyacentes_rec(grafo, n, vertices, v_actual,verticesNoAdyacentes):
    if(len(verticesNoAdyacentes) == n):
        if not (no_es_compatible(verticesNoAdyacentes,grafo)):
            return verticesNoAdyacentes
        else:
            return None
    if(v_actual == len(vertices)):
        return None
    
    verticesNoAdyacentes.append(vertices[v_actual])
    con = no_adyacentes_rec(grafo,n,vertices,v_actual+1,verticesNoAdyacentes)
    if con:
        return con
    verticesNoAdyacentes.remove(vertices[v_actual])
    sin = no_adyacentes_rec(grafo,n,vertices,v_actual+1,verticesNoAdyacentes)
    return sin

def no_es_compatible(verticesNoAdyacentes,grafo):
    for v in verticesNoAdyacentes:
        for w in verticesNoAdyacentes:
            if v == w:
                continue
            if grafo.estan_unidos(v,w):
                return True
    return False

if __name__ == "__main__":
    g = Grafo.Grafo()
    g.agregar_arista('A', 'B', 1)
    g.agregar_arista('B', 'C', 1)
    g.agregar_arista('C', 'D', 1)
    g.agregar_arista('D', 'A', 1)

    print(no_adyacentes(g,4))

    