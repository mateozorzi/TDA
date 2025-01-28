import grafo

def knight_tour(n):
    g = grafo.Grafo()
    for i in range(n):
        for j in range(n):
            g.agregar_vertice((i, j))

    for i in range(n):
        for j in range(n):
            for k in [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
                nueva_i = i + k[0]
                nueva_j = j + k[1]

                if 0 <= nueva_i < n and 0 <= nueva_j < n:
                    g.agregar_arista((i, j), (nueva_i, nueva_j), 1)

    camino = []
    vertices = g.obtener_vertices()

    return knight_tour_bt(g, vertices, 0, camino, n, 0)


def knight_tour_bt(g, vertices, actual, camino, n, vInicio):
    if actual >= len(vertices):
        return False

    while actual < len(vertices):
        if vertices[actual] not in camino:
            camino.append(vertices[actual])
            if len(camino) == len(vertices) and esCompatible(g, camino):
                return True
            elif esCompatible(g, camino):
                if knight_tour_bt(g, vertices, 0, camino, n, vInicio):
                    return True
            camino.remove(vertices[actual])
        actual += 1

    if actual >= len(vertices) and len(camino) != len(vertices) and vInicio < len(vertices):
        camino = []
        actual = vInicio + 1
        vInicio += 1
        return knight_tour_bt(g, vertices, actual, camino, n, vInicio)

    return False

    
def esCompatible(g, camino):
    if len(camino) >= 2:
        if g.estan_unidos(camino[-2], camino[-1]):
            return True
        else:
            return False
    else:
        return True

print(knight_tour(5))
