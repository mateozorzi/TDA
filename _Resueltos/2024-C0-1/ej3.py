import grafo as grafo

def esKCore(grafo,k):
    for v in grafo.obtener_vertices():
        if len(grafo.adyacentes(v)) < k:
            return False
    
    return

def kCore(grafo, k):
    vertices = grafo.obtener_vertices()
    #vertices = sorted(vertices, key=lambda x: len(grafo.adyacentes(x)), reverse=True)

    kcore = []

    for v in vertices:
        contador = 0
        if len(grafo.adyacentes(v)) >= k:
            for w in vertices:
                if v == w:
                    continue
                if grafo.estan_unidos(v,w) and len(grafo.adyacentes(w)) > k:
                    contador += 1
            if contador >= k:
                kcore.append(v)
    return kcore
    #grafoKCore = grafo.Grafo()


g = grafo.Grafo()
g.agregar_arista('A','B',1)
g.agregar_arista('A','C',1)
g.agregar_arista('B','C',1)
g.agregar_arista('B','D',1)
g.agregar_arista('B','E',1)
g.agregar_arista('C','E',1)
g.agregar_arista('D','E',1)
g.agregar_arista('D','F',1)

print(kCore(g,3))

    
            

