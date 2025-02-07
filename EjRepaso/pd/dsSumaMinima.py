import grafo

def buscarOptimos(grafo, vertices):
    optimos = [0] * (len(vertices)+1)
    #casos base
    optimos[1] = int(vertices[0])
    optimos[2] = min(int(vertices[0]), int(vertices[1]))

    #Ec de recurrencia
    #si agrego v_actual, veo el optimo anterior
    #si no agrego el v_actual, tengo que agregar el anterior a este con el optimo anteanterior
    #optimos[i] = min(v[i-2] + optimos[i-2], v[i-1] + optimos[i-2])

    for i in range(3, len(optimos)):
        optimos[i] = min(vertices[i-1] + optimos[i-1], vertices[i-1] + optimos[i-2],
                         vertices[i-2] + optimos[i-2])

    return optimos
    
def reconstruccion(grafo, vertices, optimos, pos, solucion):
    if pos <= 0:
        return solucion
    
    if vertices[pos-1] + optimos[pos-1] == optimos[pos]:
        solucion.append(vertices[pos-1])
        #puedo llegar a agregar el anterior
        return reconstruccion(grafo, vertices, optimos,pos-1, solucion)
    elif vertices[pos-1] + optimos[pos-2] == optimos[pos]:
        solucion.append(vertices[pos-1])
        #no voy a agregar el anterior
        return reconstruccion(grafo, vertices, optimos,pos-2,solucion)
    elif vertices[pos-2] + optimos[pos-2] == optimos[pos]:
        solucion.append(vertices[pos-2])
        return reconstruccion(grafo, vertices, optimos, pos-2, solucion)

def ds_suma_minima(grafo):
    vertices = grafo.obtener_vertices()
    optimos = buscarOptimos(grafo, vertices)

    solucion = []
    solucion = reconstruccion(grafo, vertices, optimos, len(optimos)-1, solucion)
    solucion = list(reversed(solucion))

    return solucion

A = grafo.Grafo()
"""A.agregar_arista(2, 4,1)
A.agregar_arista(4, 3,1)
A.agregar_arista(3, 1,1)"""
"""A.agregar_arista(3, 2,1)
A.agregar_arista(2, 5,1)
A.agregar_arista(5, 10,1)
A.agregar_arista(10, 7,1)"""

vertices1 = [4, 1, 3, 7, 8, 2]
A.agregar_arista(4, 1,1)
A.agregar_arista(1, 3,1)
A.agregar_arista(3, 7,1)
A.agregar_arista(7, 8,1)
A.agregar_arista(8, 2,1)


print(ds_suma_minima(A))