"""
Dado un tablero de ajedrez n x n, implementar un algoritmo por backtracking que ubique (si es posible) a n reinas de tal manera que ninguna pueda comerse con ninguna.

Nota: el ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo, está disponible como se describe.
"""

import grafo


def crear_grafo(n):
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
    
    return g

def es_compatible(grafo, parcial, actual):
    for p in parcial:
        if grafo.estan_unidos(p, actual):
            return False
        
    return True

def nreinas_bt(grafo, vertices, n, parcial, solucion, indice):
    if len(parcial) == n:
        solucion = parcial[:]
        return solucion
    
    if indice >= len(vertices):
        return solucion

    if es_compatible(grafo, parcial, vertices[indice]):
        parcial.append(vertices[indice])
        solucion = nreinas_bt(grafo, vertices, n , parcial, solucion, indice+1)
        parcial.pop()
    solucion = nreinas_bt(grafo, vertices, n, parcial, solucion, indice+1)

    return solucion

def nreinas(n):
    grafo = crear_grafo(n)

    parcial = []
    solucion = []

    indice = 0

    solucion = nreinas_bt(grafo, grafo.obtener_vertices(), n, parcial, solucion, indice)
    
    if len(solucion) == n:
        return solucion
    return None