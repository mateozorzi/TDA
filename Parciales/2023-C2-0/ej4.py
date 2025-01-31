def esDM(grafo, vertices,k):
    if len(vertices) > k:
        return False
    
    conjunto = set(vertices)

    for v in grafo.obtener_vertices():
        if v in conjunto:
            continue
        adyacentes = grafo.adyacentes(v)
        esAdyacente = False
        for ady in adyacentes:
            if ady in conjunto:
                esAdyacente = True

        if not esAdyacente:
            return False
    
    return True

def dominating_set_bt(grafo,vertices,parcial,minimo,indice,k):
    if len(minimo) == 0 and esDM(grafo,parcial,k):
        minimo = parcial.copy()
        return minimo
    
    if len(parcial) <= len(minimo) and esDM(grafo,parcial,k):
        minimo = parcial.copy()
        return minimo
    
    if indice == len(vertices):
        return minimo

    parcial.append(vertices[indice])
    minimo = dominating_set_bt(grafo,vertices,parcial,minimo,indice+1,k)
    parcial.pop()
    minimo = dominating_set_bt(grafo,vertices,parcial,minimo,indice+1,k)

    return minimo

def dominating_set(grafo,k):
    parcial = []
    minimo = []
    indice = 0
    vertices = grafo.obtener_vertices()
    
    minimo = dominating_set_bt(grafo,vertices,parcial,minimo,indice,k)

    return minimo