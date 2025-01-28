import grafo

#si encuentro que el grafo es adyacente, devuelvo True
def esAdyacente(grafo, vertice, conjunto):
    for w in conjunto:
        if vertice in grafo.adyacentes(w):
            return True
    
    return False

# me fijo que para todo vertice v del grafo, este pertenece al conjunto o es adyacnete a algun vertice del conjunto
def esValido(grafo, vertices,conjunto):
    for v in vertices:
        if v not in conjunto and not esAdyacente(grafo,v,conjunto):
            return False
    return True


def ds_bt(grafo, vertices, indice, conjunto, minimo):
    if len(minimo) == 0 and esValido(grafo, vertices,conjunto):
        minimo = conjunto.copy()
        return minimo

    if len(conjunto) > 0 and len(conjunto) < len(minimo) and esValido(grafo, vertices,conjunto):
        minimo = conjunto.copy()
        return minimo

    if indice == len(vertices):
        return minimo

    conjunto.append(vertices[indice])
    minimo = ds_bt(grafo, vertices, indice+1, conjunto, minimo)
    conjunto.pop()
    minimo = ds_bt(grafo, vertices, indice+1, conjunto, minimo)

    return minimo

def dominating_set_min(grafo):
    vertices = grafo.obtener_vertices()

    conjunto = []
    minimo = []
    indice = 0

    minimo = ds_bt(grafo,vertices, indice, conjunto, minimo)
    
    return  minimo

grafo = grafo.Grafo()
grafo.agregar_arista('A','B',1)
grafo.agregar_arista('A','D',1)
grafo.agregar_arista('B','C',1)
grafo.agregar_arista('C','D',1)
grafo.agregar_arista('C','E',1)
grafo.agregar_arista('E','D',1)

print(dominating_set_min(grafo))