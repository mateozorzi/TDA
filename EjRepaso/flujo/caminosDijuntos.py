import grafo
"""
Implementar un algoritmo que dado un grafo no dirigido y conexo, un vértice v y otro w, determine la cantidad
máxima de caminos disjuntos, y cómo son, que conectan a v con w. Indicar y justificar la complejidad del algoritmo
implementado
"""

def FF(grafo,v,w):
    flujo = {}
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            flujo[(v,w)] = 0
    grafo_residual = grafo.copy()

    camino = obtener_camino(grafo_residual,v,w)
    while camino != None:
        peso = peso_minimo_camino(grafo_residual, camino)

        for i in range(1, len(camino)):
            if grafo_residual.estan_unidos(camino[i-1], camino[i]):
                flujo[(camino[i-1], camino[i])] += peso
            else:
                flujo[(camino[i], camino[i-1])] -= peso
 
            actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], peso)
        
        camino = obtener_camino(grafo_residual,v,w)
    
    return flujo

def crearGrafoDirigido(grafo, fuente, sumidero):
    grafo_dirigido = grafo.Grafo(True)
    for v in grafo.obtener_vertices():
        grafo_dirigido.agregar_vertice(v)
    
    for v in grafo.obtener_vertices():
        if v == sumidero:
            continue
        for w in grafo.adyacentes(v):
            if w == fuente:
                continue
            grafo_dirigido.agregar_arista(v,w,1)
            x = f"{v}-{w}"
            grafo_dirigido.agregar_vertice(x) #arista para evitar ciclos
            grafo_dirigido.agregar_arista(v,x,1)
            grafo_dirigido.agregar_arista(x,w,1)
    
    return grafo_dirigido

def obtener_caminos_dijuntos(grafo,v,w, flujo):
    camino = []
    visitados = set()
    padres = {}
    cola = Heap()

    visitados.add(v)
    cola.push(v)
    padres[v] = None

    while cola.notEmpty():
        vertice = cola.pop()

        if vertice == w:
            break

        for k in grafo.adyacentes(vertice):
            if (vertice,k) in flujo and flujo[(vertice,k)] == 0: #me fijo que no se haya usado la arista
                continue
            if k in visitados: 
                continue
            visitados.add(k)
            padres[k] = vertice
            cola.push(k)
    
    if w not in visitados:
        return None
    
    camino = []
    vertice = w
    while vertice != None:
        camino.append(vertice)
        flujo[(padres[vertice],vertice)] = 0
        vertice = padres[vertice]
    
    camino.reverse()
    
    return camino, flujo

def caminos_dijuntos(grafo,v,w):
    grafo_dirigido = crearGrafoDirigido(grafo,v,w)

    flujo = FF(grafo_dirigido,v,w)

    caminos = []
    camino, flujo = obtener_caminos_dijuntos(grafo_dirigido,v,w, flujo)
    while camino != None:
        caminos.append(camino)
        camino, flujo = obtener_caminos_dijuntos(grafo_dirigido,v,w, flujo)
    
    return caminos, len(caminos)
        
