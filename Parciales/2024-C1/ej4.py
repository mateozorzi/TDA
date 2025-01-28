import grafo

def sumaVertices(parcial):
    aux = 0
    for v in parcial:
        aux += v
    return aux

def esDM(parcial,vertices,grafo):
    for v in vertices:
        if v not in parcial and all(v not in grafo.adyacentes(p) for p in parcial):
            return False
    return True

def DMsumaMinimaBT(grafo,vertices,indice,minimo,parcial,sol):
    if esDM(parcial,vertices,grafo) and minimo[0] > sumaVertices(parcial):
        sol[:] = parcial[:]
        minimo[0] = sumaVertices(parcial)
    


    if indice >= len(vertices) or minimo[0] < sumaVertices(parcial):
        return
    
    parcial.append(vertices[indice])
    DMsumaMinimaBT(grafo,vertices,indice+1,minimo,parcial,sol)
    parcial.remove(vertices[indice])
    DMsumaMinimaBT(grafo,vertices,indice+1,minimo,parcial,sol)
    
    return sol




def DMsumaMinima(grafo):
    vertices = grafo.obtener_vertices()
    sol = []
    parcial = []
    minimo = [0]
    for v in vertices:
        minimo[0] += v
    
    sol = DMsumaMinimaBT(grafo,vertices,0,minimo,parcial,sol)

    return sol

A = grafo.Grafo()
A.agregar_arista(3, 8,1)
A.agregar_arista(8, 1,1)
A.agregar_arista(8, 2,1)
A.agregar_arista(1, 4,1)
print(DMsumaMinima(A))

