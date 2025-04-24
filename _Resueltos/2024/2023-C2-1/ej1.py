import grafo

def esVC(grafo,vcParcial,vertices):
    for v in vertices:
        for w in grafo.adyacentes(v):
            if v not in vcParcial or w not in vcParcial:
                return False
    
    return True

def vertex_cover_bt(grafo,vertices,indice,parcial,minimo):
    if len(minimo) == 0 or len(minimo) > len(parcial):
        if esVC(grafo,parcial,vertices):
            minimo[:] = parcial[:]
    
    if indice >= len(vertices) or (len(parcial) > len(minimo) and len(minimo) == 0):
        return
    
    parcial.append(vertices[indice])
    vertex_cover_bt(grafo,vertices,indice+1,parcial,minimo)
    parcial.remove(vertices[indice])
    vertex_cover_bt(grafo,vertices,indice+1,parcial,minimo)

    return minimo

def vertex_cover(grafo):
    vertices = grafo.obtener_vertices()
    parcial = []
    minimo = []

    vertex_cover_bt(grafo,vertices,0,parcial,minimo)
    return minimo



