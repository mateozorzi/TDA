"""
Decimos que dos caminos son disjuntos si no comparten aristas (pueden compartir nodos). Dado un grafo dirigido y dos vértices s y t, 
encontrar el máximo número de caminos disjuntos s-t en G. 
Dar una metodología, explicando en detalle cómo se modela el problema, cómo se lo resuelve y cómo se consigue el máximo número de caminos disjuntos. 
¿Cuál es el orden temporal de la solución implementada?
*cambio mio: Dado un grafo no dirigido*
"""
from grafo import *
from ford_fulkerson import ff
from bfs import bfs

def grafo_dirigido(g,fuente, sumidero):
    grafo = Grafo()
    visitados = {}
    ficticios = {}
    for v in g.obtener_vertices():
        for ady in g.adyacentes(v):
            if ady in visitados:
                continue
            if v == fuente:
                grafo.agregar_arista(v,ady, 1)
            elif v == sumidero:
                grafo.agregar_arista(ady,v, 1)
            else:
                grafo.agregar_vertice(v+ady)
                ficticios.add(v/ady)
                grafo.agregar_arista(v,ady, 1)
                grafo.agregar_arista(ady, v+ady, 1)
                grafo.agregar_arista(v+ady, v, 1)
        visitados.add(v)

    return grafo, ficticios

def caminos_dijuntos(g, fuente, sumidero):
    grafo, ficticios = grafo_dirigido(g,fuente, sumidero) #O(V+E)

    flujo = ff(grafo, fuente, sumidero) #todas las aristas de peso 1 -> O(V+E)

    #tengo que recrear los caminos
    # corregimos los flujos para que se cancelen si van ida y vuelta:
    for ficticio in ficticios: #O(V)
        v = ficticios[ficticio].split("/")[0]
        w = ficticios[ficticio].split("/")[1]
        if flujo[(v,w)] == 1 and flujo[(v+w,v)] == 1:
            flujo[(v,w)] = 0
            flujo[(w,v+w)] = 0
            flujo[(v+w,v)] = 0

    caminos = []
    cant_caminos = 0
    for ady in grafo.vertices(fuente): #O(E)
        cant_caminos += grafo.peso_arista(fuente, ady)

    for _ in range(cant_caminos): #O(V + E)
        camino = []
        camino.append(fuente)
        actual = fuente

        while actual != sumidero: 
            for ady in grafo.adyacentes(actual):
                if flujo[(actual, ady)] == 1:
                    flujo[(actual, ady)] = 0
                    if ady not in ficticios:
                        camino.append(ady)
                    actual = ady
                    break

        caminos.append(camino)
    





                


    