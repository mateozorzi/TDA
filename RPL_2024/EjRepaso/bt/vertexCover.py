import grafo

def esVC(grafo, vertices, conjunto):
    for v in vertices:
        for w in grafo.adyacentes(v):
            if v == w:
                continue
            if v not in conjunto and w not in conjunto:
                return False
    
    return True

def vc_bt(grafo,vertices,indice,parcial,minimo):
    if len(minimo) == 0 and esVC(grafo,vertices,parcial):
        minimo = parcial.copy()
        return minimo
    
    if len(parcial) > 0 and len(parcial) < len(minimo) and esVC(grafo,vertices,parcial):
        minimo = parcial.copy()
        return minimo
    
    if indice == len(vertices):
        return minimo

    parcial.append(vertices[indice])
    minimo = vc_bt(grafo, vertices, indice+1, parcial, minimo)
    parcial.pop()
    minimo = vc_bt(grafo, vertices, indice+1, parcial, minimo)

    return minimo

def vertex_cover_min(grafo):
    vertices = grafo.obtener_vertices()

    parcial = []
    minimo = []
    indice = 0

    minimo = vc_bt(grafo, vertices, indice, parcial, minimo)

    return minimo

grafo = grafo.Grafo()
grafo.agregar_vertice(1)
grafo.agregar_vertice(2)
grafo.agregar_vertice(3)
grafo.agregar_vertice(4)

grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 4)
grafo.agregar_arista(4, 1)

ciclo = vertex_cover_min(grafo)
print(ciclo)