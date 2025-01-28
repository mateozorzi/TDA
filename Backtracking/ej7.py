"""Implementar un algoritmo de backtracking que, dado una pieza de caballo en un tablero de ajedrez de n x n, 
determine si existen los movimientos a realizar para que el caballo logre pasar por todos los casilleros del tablero una única vez.
Recordar que el caballo mueve en forma de L (dos casilleros en una dirección, y un casillero en forma perpendicular)."""
import grafo
def knight_tour(n):
    g = grafo.Grafo()
    aristas_agregadas = set()  # Conjunto para mantener aristas únicas

    for i in range(n):
        for j in range(n):
            g.agregar_vertice((i, j))

    for i in range(n):
        for j in range(n):
            for k in [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
                nueva_i = i + k[0]
                nueva_j = j + k[1]

                if 0 <= nueva_i < n and 0 <= nueva_j < n:
                    arista = ((i, j), (nueva_i, nueva_j))
                    arista2 = ((nueva_i, nueva_j), (i, j))
                    if arista not in aristas_agregadas and arista2 not in aristas_agregadas:
                        g.agregar_arista((i, j), (nueva_i, nueva_j), 1)
                        aristas_agregadas.add(arista)
                
    
    
    camino = []
    vertices = g.obtener_vertices()

    for v in vertices:
        camino = []
        if knight_tour_bt(g,v,camino,n):
            return True
    return False
    
def knight_tour_bt(g,vertice,camino,n):
    camino.append(vertice)
    if len(camino) == n**2 and esCompatible(g,camino):
        return True
    
    for ady in g.adyacentes(vertice):
        if ady not in camino and esCompatible(g,camino):    
            if knight_tour_bt(g,ady,camino,n):
                return True
    camino.pop()
    return False

    
def esCompatible(g,camino):  
    if len(camino) >= 2:    
        if(g.estan_unidos(camino[-2],camino[-1])):
            return True
        else:
            return False
    else:
        return True
    

print(knight_tour(6))