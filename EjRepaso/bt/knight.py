import grafo

def crearTablero(n):
    g = grafo.Grafo()
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            g.agregar_vertice(f"{i},{j}")
    
    #adyacencias por el movimiento del caballo
    for v in g.obtener_vertices():
        fila = int(v.split(",")[0])
        columna = int(v.split(",")[1])
        
        for w in g.obtener_vertices():
            if v == w:
                continue
            fila_w  = int(w.split(",")[0])
            columna_w = int(w.split(",")[1])

            if abs(fila - fila_w) == 2 and abs(columna - columna_w) == 1 and not g.estan_unidos(v,w):
                g.agregar_arista(v,w,1)
            elif abs(fila - fila_w) == 1 and abs(columna - columna_w) == 2 and not g.estan_unidos(v,w):
                g.agregar_arista(v,w,1)

    return g

def esValido(g,visitados):
    #la conexion debe ser por las adyacencias creadas
    casilleroActual = visitados[-1]
    casilleroAnterior = visitados[-2]

    if not g.estan_unidos(casilleroActual,casilleroAnterior): #no pude haber saltado de un casillero a otro
        return False
    
    return True
        
            

def knight_tour_bt(t, casilleros, casilla, visitados, camino):
    visitados.append(casilla)
    camino.append(casilla)
    if len(visitados) > 1 and not esValido(t,visitados):
        return camino
    
    if len(visitados) == len(casilleros):
        return camino

    for ady in t.adyacentes(casilla):
        if ady not in visitados:
            camino = knight_tour_bt(t, casilleros, ady, visitados, camino)
            if len(visitados) == len(casilleros):
                return camino
    visitados.remove(casilla)
    camino.pop()
    return camino

def knight_tour(n):
    t = crearTablero(n)
    casilleros = t.obtener_vertices()
    indice = 0

    visitados = []
    camino = []

    for v in t.obtener_vertices():
        knight_tour_bt(t, casilleros, v, visitados, camino)
        if camino:
            break


    if len(visitados) == len(casilleros):
        return True
    return False

n = 5
print(knight_tour(n)) #True