import grafo

def buscarOptimos(grafo, vertices):
    optimos = [0] * (len(vertices)+1)
    #casos base
    optimos[0] = int(vertices[0])
    optimos[1] = min(int(vertices[0]), int(vertices[1]))

    #Ec de recurrencia
    #optimos[i] = 
    

def ds_suma_minima(grafo):
    vertices = grafo.obtener_vertices()
    optimos = buscarOptimos(grafo, vertices)

    return 0