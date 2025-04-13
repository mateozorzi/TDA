"""Un set dominante (Dominating Set) de un grafo G es un subconjunto D de vértices de G, 
tal que para todo vértice de G: o bien
(i) pertenece a D;
o bien (ii) es adyacente a un vértice en D.

Implementar un algoritmo que reciba un Grafo, 
y devuelva un dominating set de dicho grafo con la mínima cantidad de vértices."""
import grafo
def dominating_set_min(grafo):
    vertices = grafo.obtener_vertices()
    indice = 0
    dominating_set = []
    minimo = []
    return dominating_set_min_bt(grafo,vertices,indice,dominating_set,minimo)

def esCompatible(grafo,dominating_set,vertices):
    for v in vertices:
        if v not in dominating_set:
            adyacentes = grafo.adyacentes(v)
            if not any(ady in dominating_set for ady in adyacentes):
                return False
    return True

def dominating_set_min_bt(grafo,vertices,indice,dominating_set,minimo):
    if (len(dominating_set) < len(minimo) or len(minimo) == 0) and len(dominating_set)>0:
        if esCompatible(grafo, dominating_set,vertices):
            minimo[:] = dominating_set[:]
        
    if(indice >= len(vertices)):
        return
    
    dominating_set.append(vertices[indice])
    dominating_set_min_bt(grafo,vertices,indice+1,dominating_set,minimo)
    dominating_set.remove(vertices[indice])
    dominating_set_min_bt(grafo,vertices,indice+1,dominating_set,minimo)

    return minimo


grafo = grafo.Grafo()
grafo.agregar_arista('A','B',1)
grafo.agregar_arista('A','D',1)
grafo.agregar_arista('B','C',1)
grafo.agregar_arista('C','D',1)
grafo.agregar_arista('C','E',1)
grafo.agregar_arista('E','D',1)

print(dominating_set_min(grafo))