def mst_kruskal (grafo):
    conjuntos = UnionFind (grafo.obtener_vertices())
    aristas = sort(obtener_aristas (grafo))
    arbol = Grafo (grafo.obtener_vertices())
    for a in aristas:
        v, w, peso = a
        if conjuntos. find(v) == conjuntos. find(w):
            continue
    arbol.agregar_arista(v, w, peso)
    conjuntos.union (v, w)
    return arbol