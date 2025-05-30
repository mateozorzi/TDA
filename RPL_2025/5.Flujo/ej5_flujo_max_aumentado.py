"""
Dado un flujo máximo de un grafo, implementar un algoritmo que, si se le aumenta en una unidad la capacidad a una artista 
por ejemplo, a una arista de capacidad 3 se le aumenta a 4, permita obtener el nuevo flujo máximo en tiempo lineal en vértices y aristas. 
Indicar y justificar la complejidad del algoritmo implementado.
"""

from ej3_crear_red_residual import red_residual
from bfs import bfs
from grafo import *

def actualizar_grafo_residual(grafo_residual, u, v, valor):
    peso_anterior = grafo_residual.peso_arista(u, v)

    if peso_anterior == valor:
        grafo_residual.remover_arista(u, v)
    else:
        grafo_residual.cambiar_peso(u, v, peso_anterior - valor)
         
    if not grafo_residual.hay_arista(v, u):
        grafo_residual.agregar_arista(v, u, valor)
    else:
	    grafo_residual.cambiar_peso(v, u, grafo_residual.peso(v, u) + valor)
        

def aumento_arista(flujo, grafo, fuente, sumidero):
    #creo red residual
    grafo_residual = red_residual(grafo, flujo) #O(V + E)      


    #hacer bfs e ir sumando el flujo en 1
    camino = bfs(grafo_residual,fuente, sumidero) #O(V + E)

    for i in range(1, len(camino)): #O(V)
        if grafo.hay_arista(camino[i-1], camino[i]):
            actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], 1)
            flujo[(camino[i-1], camino[i])] += 1
        else:
            actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], 1)
            flujo[(camino[i], camino[i-1])] -= 1

    return flujo
