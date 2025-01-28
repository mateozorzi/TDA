import grafo
def nreinas(n):
    g = grafo.Grafo()
    for i in range(n):
        for j in range(n):
            g.agregar_vertice((i, j))

    # Agrego adyacencia por fila
    for i in range(n):
        for j in range(n):
            for k in range(j + 1, n):
                g.agregar_arista((i, j), (i, k))
    # Agrego por columnas
    for j in range(n):
        for i in range(n):
            for k in range(i+1, n):
                g.agregar_arista((i, j), (k, j))

    # agrego por diagonales
    for i in range(n):
        for j in range(n):
            for k in range(i):
                if k < j:
                    g.agregar_arista((i, j), (i - k - 1, j - k - 1))
                if k + j + 1 < n:
                    g.agregar_arista((i, j), (i - k - 1, j + k + 1))
    
    
    reinas = []
    vertices = g.obtener_vertices()
    
    return nreinas_bt(g,vertices, 0, reinas,n)

def nreinas_bt(g,vertices,actual,reinas,n):
    if actual == len(vertices) and len(reinas) != n:
        return []
    
    if(len(reinas) == n):
        if esCompatible(g,reinas):
            return reinas
        else:
            return []
        
    if not esCompatible(g,reinas):
        return[]


    reinas.append(vertices[actual])
    conSig = nreinas_bt(g,vertices,actual+1,reinas,n)
    if conSig:
        return conSig
    reinas.remove(vertices[actual])
    sinSig = nreinas_bt(g,vertices,actual+1,reinas,n)

    return conSig + sinSig

def esCompatible(g,vertices):
    for v in vertices:
        for w in vertices:
            if v == w:
                continue
            elif(g.estan_unidos(v,w)):
                return False

    return True


print(nreinas(4))