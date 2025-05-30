"""
Dada una red y un diccionario que representa los valores de los flujos para las aristas, todos valores que respetan la restricción de cada arista, 
construir la red residual que refleja el estado actual de la red en función a los valores de flujo dados.
"""
from grafo import *
def red_residual(grafo, flujo):
    grafo_residual = Grafo()

    for vertice in grafo.obtener_vertices(): #O(V)
        grafo_residual.agregar_vertice(vertice)

    for (u,v) in flujo: #O(E)
        flujo_arista = flujo[(u,v)]
        valor_original = grafo.peso_arista(u,v)
        grafo_residual.agregar_arista(u,v,valor_original-flujo_arista)
        grafo_residual.agregar_arista(v,u, flujo_arista)

    return grafo_residual


