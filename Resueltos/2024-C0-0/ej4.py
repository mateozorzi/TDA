def hayCamino(grafo,s,t):
    #BFS
    return

def obtenerPesoMinimo(grafo, camino):
    #devuelvo la capicidad minima restante de las aristas
    return

def actualizarGrafoResidual(grafo,v,w,peso):
    #actualizo arista (v,w)

    #actualizo arista (w,v)

    return


def fordFulkerson(grafo,s,t):
    flujo = {}

    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes():
            flujo[(v,w)] = 0

    grafoResidual = grafo.copiar()

    while hayCamino(grafoResidual,s,t) is not None:
        camino = hayCamino(grafoResidual,s,t)
        pesoMinimo = obtenerPesoMinimo(grafoResidual, camino)
        for i in range(1,len(camino)):
            if grafo.estan_unidos(camino[i-1], camino[i]):
                flujo[(camino[i-1], camino[i])] += pesoMinimo
                actualizarGrafoResidual(grafoResidual, camino[i-1], camino[i], pesoMinimo)
            else:
                flujo[(camino[i-1], camino[i])] -= pesoMinimo
                actualizarGrafoResidual(grafoResidual, camino[i-1], camino[i], pesoMinimo)
    
    return flujo


def ataque(grafo):
    vertices = grafo.obtener_vertices()
    flujoMaximo = fordFulkerson(grafo,vertices[0], vertices[-1])
    tuberiaMaximo = flujoMaximo[0]
    maximo = flujoMaximo[tuberiaMaximo]

    for tuberia in flujoMaximo:
        if flujoMaximo[tuberia] > maximo:
            tuberiaMaximo = tuberia
            maximo = flujoMaximo[tuberia]
    
    return tuberiaMaximo