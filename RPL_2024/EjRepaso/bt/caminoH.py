import grafo

def camino_h_bt(grafo, v, visitados, solucion):
    solucion.append(v)
    visitados.add(v)
    if len(visitados) == len(grafo.obtener_vertices()):
            return solucion
   
    for ady in grafo.adyacentes(v):
        if ady not in visitados:
            camino_h_bt(grafo, ady, visitados, solucion)
            if len(visitados) == len(grafo.obtener_vertices()):
                return solucion
    
    visitados.remove(v)
    solucion.pop()

    return None


def camino_H(grafo):
    solucion = []
    visitados = set()
    vertices = grafo.obtener_vertices()
    
    for v in vertices:
        if camino_h_bt(grafo, v, visitados, solucion) != None:
            return solucion

    return None


g = grafo.Grafo()
g.agregar_arista('0','2',1)
g.agregar_arista('0','4',1)
g.agregar_arista('0','5',1)
g.agregar_arista('1','4',1)
g.agregar_arista('1','5',1)
g.agregar_arista('2','0',1)
g.agregar_arista('2','4',1)
g.agregar_arista('3','4',1)
g.agregar_arista('4','0',1)
g.agregar_arista('4','1',1)
g.agregar_arista('4','2',1)
g.agregar_arista('4','3',1)
g.agregar_arista('4','5',1)
g.agregar_arista('5','0',1)
g.agregar_arista('5','1',1)
g.agregar_arista('5','4',1)
print(camino_H(g))