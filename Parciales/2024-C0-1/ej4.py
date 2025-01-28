import grafo

def grafo_tres_sat(clausulas):
    g = grafo.Grafo()
    
    #creo los vertices para cada termino de las clausulas
    for clausula in clausulas:
        for termino in clausula:
            if termino not in g.obtener_vertices():
                g.agregar_vertice(termino)

    #uno vertices, en relacion a las clausulas
    for clausula in clausulas:
        for t1 in clausula:
            for t2 in clausula:
                if t1 == t2:
                    continue
                if not g.estan_unidos(t1,t2):
                    g.agregar_arista(t1,t2,1)

    #uno los vertices complementos
    for v in g.obtener_vertices():
        if v.startswith("not "):
            complemento = v[4:]  # Quitar el "not "
        else:
            complemento = "not " + v
        if complemento in g.obtener_vertices():
            g.agregar_arista(v, complemento)
    
    return g

def esIS(grafo,terminos):
    for t1 in terminos:
        for t2 in grafo.adyacentes(t1):
            if t2 in terminos:
                return False
    return True

def tres_sat_bt(grafo,k,vertices,terminos,indice):
    if not esIS(grafo,terminos):
        return []
    if len(terminos) >= k:
        return terminos
    
    if indice >= len(vertices):
        return []
    
    terminos.append(vertices[indice])
    con = tres_sat_bt(grafo,k,vertices,terminos,indice+1)
    if con:
        return con
    terminos.remove(vertices[indice])
    sin = tres_sat_bt(grafo,k,vertices,terminos,indice+1)

    return sin

def tres_sat(grafo,k):
    vertices = grafo.obtener_vertices()
    terminos = []

    return tres_sat_bt(grafo,k,vertices,terminos,0)

clausulas = [
    ["X1", "not X2", "X3"],
    ["not X1", "X5", "X8"],
    ["X4", "X6", "not X7"],
    ["X9", "not X1", "not X5"]
]

g = grafo_tres_sat(clausulas)
print(tres_sat(g, len(clausulas)))

