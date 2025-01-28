import grafo

def sigoAgregando(grafo, ciclo, v, k):
    if len(ciclo) < k-1:
        return True #Todavia no tengo que cerrar el ciclo
    return False

def ciclo_bt(grafo, vertices,v,ciclo,k, vertice_inicio, ciclo_konseguido):
    if len(ciclo_konseguido) == k: #si ya encontre un ciclo de k aristas, no sigo buscando
        return ciclo_konseguido
    
    if len(ciclo) == k and ciclo[0] == ciclo[-1]: #se cerro el ciclo
        ciclo_konseguido = ciclo.copy()
        return ciclo_konseguido
    
    if len(ciclo) == (k-1) and v != vertice_inicio: #si estoy en el ultimo vertice y no puedo cerrar el ciclo
        return ciclo_konseguido
    
    ciclo.append(v)
    if sigoAgregando(grafo, ciclo, v, k):    
        for ady in grafo.adyacentes(v): 
            if ady == vertice_inicio:
                continue #Si me encuentro el vertice de inicio, y todavia no cierro el ciclo lo salteo
            if ady not in ciclo:   #si el vertice no esta en el ciclo pruebo agregandolo
                ciclo_konseguido = ciclo_bt(grafo,vertices,ady,ciclo,k, vertice_inicio, ciclo_konseguido)
                ciclo.pop()
                ciclo_konseguido = ciclo_bt(grafo,vertices,ady,ciclo,k, vertice_inicio, ciclo_konseguido)
    elif len(ciclo) < k: #veo si puedo cerrar el ciclo
        if vertice_inicio in grafo.adyacentes(v):
            ciclo_konseguido = ciclo_bt(grafo,vertices,vertice_inicio,ciclo,k, vertice_inicio, ciclo_konseguido)

    return ciclo_konseguido

#devolver un ciclo de exactamente k aristas en un grafo no dirigido
def ciclo_k(grafo,k):
    vertices = grafo.obtener_vertices()

    ciclo = []
    ciclo_konseguido = []
    
    for v in vertices:
        vertice_inicio = v
        ciclo_konseguido = ciclo_bt(grafo,vertices,v,ciclo,k, vertice_inicio, ciclo_konseguido)
        if len(ciclo_konseguido) == k:
            return ciclo_konseguido
        
    return None
        
        


grafo = grafo.Grafo()
grafo.agregar_vertice(1)
grafo.agregar_vertice(2)
grafo.agregar_vertice(3)
grafo.agregar_vertice(4)

grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 4)
grafo.agregar_arista(4, 1)

# Ahora puedes usar este grafo con la función ciclo_k
k = 3
ciclo = ciclo_k(grafo, k)
print(ciclo)