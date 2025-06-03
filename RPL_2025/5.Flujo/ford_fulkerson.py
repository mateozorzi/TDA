from grafo import *
from bfs import bfs

def copiar(grafo):
    vertices = grafo.obtener_vertices()

    g = Grafo(True)
    for v in vertices:
        for w in vertices:
            g.agregar_arista(v,w)

    return g

def peso_minimo_camino(grafo, camino):
    minimo = grafo.peso_arista(camino[0], camino[1])
    for i in range(1, len(camino)):
        peso = grafo.peso_arista(camino[i-1], camino[1])
        minimo = min(minimo, peso)
    
    return minimo

def actualizar_grafo_residual(grafo, u, v, valor):
    peso_anterior = grafo.peso_arista(u, v)

    if peso_anterior == valor:
        grafo.remover_arista(u, v)
    else:
        grafo.cambiar_peso(u, v, peso_anterior - valor)
         
    if not grafo.hay_arista(v, u):
        grafo.agregar_arista(v, u, valor)
    else:
	    grafo.cambiar_peso(v, u, grafo.peso(v, u) + valor)

def ff(grafo, s, t):
    flujo = {}
    vertices = grafo.obtener_vertices()

    for v in vertices:
        for w in vertices:
            flujo[(v,w)] = 0
    
    grafo_residual = copiar(grafo)

    camino = bfs(grafo_residual,s,t)
    while camino != None:
        peso_min = peso_minimo_camino(grafo_residual, camino)

        for i in range(1, len(camino)):
            if grafo_residual.estan_unidos(camino[i-1], camino[i]):
                flujo[(camino[i-1], camino[i])] += peso_min
                actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], peso_min)
            else:
                flujo[(camino[i], camino[i-1])] -= peso_min
                actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], peso_min)
        
        camino = bfs(grafo_residual,s,t)


