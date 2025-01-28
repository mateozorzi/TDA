"""Dada una red y un diccionario que representa los valores de los flujos para las aristas, todos valores que respetan la restricción de cada arista, construir la red residual que refleja el estado actual de la red en función a los valores de flujo dados."""

def actualizar_grafo_residual (grafo_residual, u, v, valor):
    peso_anterior = grafo_residual.peso(u, v)
    if peso_anterior == valor:
        grafo_residual. remover_arista(u, v)
    else:
        grafo_residual. cambiar_peso(u, v, peso_anterior - valor)
    
    #actualizo arista opuesta
    if not grafo_residual.hay_arista(v, u):
        grafo_residual.agregar_arista(v, u, valor)
    else:
        grafo_residual. cambiar_peso(v, u, grafo_residual.peso(v, u) + valor)

def estado_actua(red, flujos):
    red_residual = red.copy()

    for nodo in red_residual:
        for ady in red_residual.adyacentes(nodo):
            actualizar_grafo_residual(red_residual, nodo, ady, flujos[(nodo,ady)])
    
    return red_residual