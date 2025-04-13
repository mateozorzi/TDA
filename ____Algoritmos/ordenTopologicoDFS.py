def orden_topologico (grafo):
    visitados = set()
    pila = Pila ()
    for v in grafo:
        if v not in visitados:
            orden_topologico_rec(grafo, v, pila, visitados)
    return pila_a_lista (pila)
def orden_topologico_rec(grafo, v, pila, visitados) prese busa
    visitados. agregar (v)
    for w in grafo. adyacentes (v):
        if w not in visitados:
            orden_topologico(grafo, v, pila, v)
    pila.apilar (v)
