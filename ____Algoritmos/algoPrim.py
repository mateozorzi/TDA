def mst_prim(grafo):
    vertice = grafo. vertice_aleatorio()
    visitados = set()
    visitados. agregar (vertice)
    q = Heap()
    arbol = Grafo (grafo.obtener_vertices())
    for w in grafo.adyacentes(v):
        q. encolar ((v, w) , grafo.peso_arista(v, w))
    while not q. esta_vacia() :
        (v, w) = q. desencolar ()
        if w in visitados:
            continue
        arbol.agregar_arista(v, w, grafo.peso_arista(v, w))
        visitados.agregar (w)
        for u in grafo. adyacentes (w) :
            if u not in visitados: 
                q. encolar ((w, u), grafo.peso_arista(w, u))
    return arbol