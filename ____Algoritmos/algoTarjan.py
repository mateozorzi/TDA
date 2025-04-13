def cfc(grafo, v, visitados, pila, apilados, orden, mas_bajo, cfcs, *indice):
    visitados.add(v)
    pila. apilar (v)
    apilados.add (v)
    Mas_bajo[v] = orden[v]
    for w in grafo.adyacentes(v):
        if w not in visitados:
            orden [w] = *indice + 1
            *indice++
            cfc(grafo, w, visitados, pila, apilados, orden, mas_bajo, cfcs)
            mas _bajo[v] = min(mas_bajo[v], mas_bajo[w])
        elif w in apilados:
            mas_bajo[v] = min (mas_bajo[v], orden[w])
    if mas_bajo[v] == orden [v]:
        nueva_cfc = []
        do:
            w = pila.desapilar()
            apilados.remove (w)
            nueva_cfc. append (w)
        while (w != v):
        cfcs. append (nueva_cfc)