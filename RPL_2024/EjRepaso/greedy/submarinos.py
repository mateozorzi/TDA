import grafo

def modelar(matriz):
    grafo = grafo.Grafo()

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            grafo.agregar_vertice(f"({i}, {j})")
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            for di in range(-2, 3):
                for dj in range(-2, 3):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < len(matriz) and 0 <= nj < len(matriz[i]) and (di != 0 or dj != 0) and not grafo.estan_unidos(f"({i}, {j})", f"({ni}, {nj})"):
                        grafo.agregar_arista(f"({i}, {j})", f"({ni}, {nj})")
    return grafo



def submarinos(matriz):
    iluminados = set()
    faros = []

    grafo = modelar(matriz)

    for v in grafo.obtener_vertices():
        xV = v.split(", ")[0][1:]
        yV = v.split(", ")[1][:-1]

        if matriz[int(xV)][int(yV)] == True:
            continue

        for w in grafo.adyacentes(v):
            xW = w.split(", ")[0][1:]
            yW = w.split(", ")[1][:-1]

            if matriz[int(xW)][int(yW)] == True and w not in iluminados:
                iluminados.add(w)
                faros.append(v)
                break

    return faros