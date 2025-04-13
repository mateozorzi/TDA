import heapq

def caminos(grafo,s,t):
    visitados = set()
    padres = {}
    q = heapq.Heap()
    visitados.add(s)
    padres[s] = None
    q.push(s)

    while not q.empty():
        #desencolo
        v = q.pop()

        #veo si es el destino
        if v == t:
            break

        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                padres[w] = v
                q.push(w)
    
    if t not in visitados:
        return None
    
    camino = []
    v = t
    while v is not None:
        camino.append(v)
        v = padres[v]
    
    camino = list(reversed(camino))

    return camino


def obtener_min_peso_camino(grafo,camino,s,t):
    pass

def actualizar_grafo_residual(grafo_residual, v, w, flujo_camino):
    pass

def ford_fulkeron(grafo, s, t):
    flujo = {}

    vertices = grafo.obtener_vertices()
    for v in vertices:
        for w in grafo.adyacentes(v):
            flujo[(v,w)] = 0
    grafo_residual = grafo.copy()
    camino = caminos(grafo_residual,s,t)
    while(camino):
        flujo_camino = obtener_min_peso_camino(grafo_residual,camino,s,t)

        for i in range(1, len(camino)):
            if grafo_residual.estan_unidos(camino[i-1], camino[i]):
                flujo[(camino[i-1], camino[i])] += flujo_camino
                actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], flujo_camino)
            else:
                flujo[(camino[i-1], camino[i])] -= flujo_camino
                actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], flujo_camino)
        
        camino = caminos(grafo_residual, s,t)
    
    return flujo

def buscar_camino(grafo,flujo, v, w):
    visitados = set()
    padres = {}
    cola = heapq.Heap()

    visitados.add(v)
    padres[v] = None
    cola.push(v)

    while cola.notEmpty():
        vertice = cola.pop()

        if vertice == w:
            break

        for ady in grafo.adyacentes(vertice):
            if ady not in visitados and flujo[(vertice, ady)] == 1:
                visitados.add(ady)
                padres[ady] = vertice
                cola.push(ady)
    
    if w not in visitados:
        return None
    
    camino = []
    actual = w
    while actual is not None:
        flujo[(padres[actual], actual)] = 0
        camino.append(actual)
        actual = padres[actual]
    
    return camino, flujo



def camino_disjuntos(grafo, v, w):
    #por flujo maximo, creo un grafo dirigo con aristas idas t vueltas(para emular un grafo no dirigido) con
    #capacidad 1 en todas las aristas. Uso ford fulkerson. El flujo maixmo es la cantidad de camino disjuntos.
    #Complejidad de FF O(A * V^2) y si todas las aristas titnen capaciad 1 -> O( A*V )
    grafoDirigido = grafo.Grafo(True)

    for v in grafo.obtener_vertices():
        grafoDirigido.agregar_vertice(v)
    
    for a in grafo.obtener_aristas():
        grafoDirigido.agregar_arista(a[0], a[1], 1)
        grafoDirigido.agregar_arista(a[1], a[0], 1)
    
    flujo = ford_fulkeron(grafoDirigido, v, w)

    cantidad_caminos = 0
    caminos = []
    camino, flujo = buscar_camino(grafoDirigido, flujo, v, w)
    while camino:
        cantidad_caminos += 1
        caminos.append(camino)
        camino, flujo = buscar_camino(grafoDirigido, flujo, v, w)

    return caminos, cantidad_caminos
