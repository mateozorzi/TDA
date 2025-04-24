import grafo
def esUnCiclo(grafo,vertices):
    adyUltimo = grafo.adyacentes(vertices[-1])
    if vertices[0] not in adyUltimo:
        return False
    
    for i in range(1,len(vertices)):
        if vertices[i] == vertices[i-1]:
            continue
        if not grafo.estan_unidos(vertices[i], vertices[i-1]):
            return False
        
    return True

def cicloGrafo_bt(grafo,k,vertices,indice,ciclo):
    if len(ciclo) > 1:
        if esUnCiclo(grafo,ciclo) and len(ciclo) == k-1:
            return ciclo
        elif len(ciclo) > k:
            return
    
    if indice >= len(vertices):
        return
    
    ciclo.append(vertices[indice])
    cicloCon = cicloGrafo_bt(grafo, k, vertices, indice+1,ciclo)
    if cicloCon:
        return ciclo
    ciclo.remove(vertices[indice])
    cicloSin = cicloGrafo_bt(grafo, k, vertices, indice+1,ciclo)

    return cicloSin


def cicloGrafo(grafo,k):
    vertices = grafo.obtener_vertices()
    indice = 0
    ciclo = []

    cicloGrafo_bt(grafo,k,vertices,indice,ciclo)

    return ciclo

g = grafo.Grafo()
g.agregar_arista('A', 'B', 1)
g.agregar_arista('B', 'C', 1)
g.agregar_arista('C', 'D', 1)

print(cicloGrafo(g,4))