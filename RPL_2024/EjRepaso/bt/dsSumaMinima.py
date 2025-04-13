def esAdy(grafo, parcial, v):
    for w in parcial:
        if grafo.estan_unidos(v,w):
            return True
    return False

def isDS(grafo, parcial):
    setConjunto = set(parcial)

    for v in grafo.obtener_vertices():
        if v in setConjunto or esAdy(grafo, parcial, v):
            continue
        return False

def ds_suma_minima_bt(grafo,vertices, indice, parcial, sol):
    if len(sol) == 0 and isDS(grafo, parcial):
        return parcial
    
    if sum(parcial) < sum(sol) and isDS(grafo, parcial):
        return parcial
    
    if sum(parcial) > sum(sol) or indice >= len(vertices):
        return sol
    
    parcial.append(vertices[indice])
    sol = ds_suma_minima_bt(grafo, vertices, indice+1, parcial, sol)
    parcial.pop()
    sol = ds_suma_minima_bt(grafo, vertices, indice+1,sol)


    return None #si llego aca no encontro nada

def ds_suma_minima(grafo):
    vertices = grafo.obtener_vertices()
    parcial = []
    sol = []
    indice = 0

    ds_suma_minima_bt(grafo,vertices, indice, parcial, sol)