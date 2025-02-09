import grafo
from bfs import bfs

def buscar_camino(grafo, s, t):
    return bfs(grafo, s, t)

def buscar_peso_minimo(grafo_residual, camino):
    peso_minimo = grafo_residual.peso(camino[0], camino[1])
    for i in range(2, len(camino)):
        peso = grafo_residual.peso(camino[i-1], camino[i])
        if peso < peso_minimo:
            peso_minimo = peso
    
    return peso_minimo

def actualizar_grafo(grafo_residual, v, w, peso):
    peso_actual = grafo_residual.peso(v,w)
    
    if peso_actual == peso:
        grafo_residual.borrar_arista(v,w)
    else:
        grafo_residual.cambiar_peso(v, w, peso_actual - peso)

    if grafo_residual.estan_unidos(w,v):
        peso_actual = grafo_residual.peso(w,v)
        grafo_residual.cambiar_peso(w,v, peso_actual + peso)
    else:
        grafo_residual.crear_arista(w,v, peso)

def FF(grafo, s, t):
    vertices = grafo.obtener_vertices()

    flujo = {}
    for v in vertices:
        for w in grafo.adyacentes(v):
            flujo[(v,w)] = 0
    
    grafo_residual = grafo.copy()
    camino = buscar_camino(grafo_residual, s, t)

    while camino != None:
        peso_minimo = buscar_peso_minimo(grafo_residual, camino)

        for i in range(1, len(camino)):
            if grafo.estan_unidos(camino[i-1], camino[i]):
                flujo[(camino[i-1], camino[i])] += peso_minimo
                actualizar_grafo(grafo_residual, camino[i-1], camino[i], peso_minimo)
            else:
                flujo[(camino[i-1], camino[i])] -= peso_minimo
                actualizar_grafo(grafo_residual, camino[i-1], camino[i], peso_minimo)

        camino = buscar_camino(grafo_residual, s, t)
    
    return flujo