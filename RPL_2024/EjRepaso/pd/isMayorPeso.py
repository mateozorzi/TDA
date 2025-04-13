import grafo

def buscarOptimos(g):
    vertices = g.obtener_vertices()
    optimos = [0] *(len(g.obtener_vertices())+1)

    #casos base:
    optimos[0] = 0
    optimos[1] = int(vertices[0])

    for i in range(1, len(optimos)):
        optimos[i] = max(optimos[i-1], optimos[i-2] + int(vertices[i-1]))

    return optimos


def is_mayor_peso(g):
    optimos = buscarOptimos(g)