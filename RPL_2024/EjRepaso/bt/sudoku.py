import grafo

#metodo crear aristas
#g.agregar_arista('A','B',1)
def crearGrafoSudoku(matriz):
    g = grafo.Grafo()

    # Crear vértices para cada celda
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            g.agregar_vertice(f"{i},{j}")

    # Adyacencias por fila
    for i in range(len(matriz)):
        for j1 in range(len(matriz[i])):
            for j2 in range(j1 + 1, len(matriz[i])):
                if not g.estan_unidos(f"{i},{j1}", f"{i},{j2}"):
                    g.agregar_arista(f"{i},{j1}", f"{i},{j2}", 1)

    # Adyacencias por columna
    for j in range(len(matriz[0])):
        for i1 in range(len(matriz)):
            for i2 in range(i1 + 1, len(matriz)):
                if not g.estan_unidos(f"{i1},{j}", f"{i2},{j}"):
                    g.agregar_arista(f"{i1},{j}", f"{i2},{j}", 1)

    # Adyacencias por región 3x3
    region_size = 3
    for region_row in range(0, len(matriz), region_size):
        for region_col in range(0, len(matriz[0]), region_size):
            # Obtener todas las celdas en esta región 3x3
            region_cells = []
            for i in range(region_row, region_row + region_size):
                for j in range(region_col, region_col + region_size):
                    region_cells.append(f"{i},{j}")
            # Conectar todas las celdas en esta región
            for idx1 in range(len(region_cells)):
                for idx2 in range(idx1 + 1, len(region_cells)):
                    if not g.estan_unidos(region_cells[idx1], region_cells[idx2]):
                        g.agregar_arista(region_cells[idx1], region_cells[idx2], 1)

    return g


def esValido(g, vertices, matriz):    
    for v in vertices:
        for w in g.adyacentes(v):
            fila_v = int(v.split(",")[0])
            columna_v = int(v.split(",")[1])
            fila_w = int(w.split(",")[0])
            columna_w = int(w.split(",")[1])
            if matriz[fila_v][columna_v] == 0 or matriz[fila_w][columna_w] == 0:
                continue
            if matriz[fila_v][columna_v] == matriz[fila_w][columna_w]:
                return False
    
    return True

def resolver_sudoku_bt(g, matriz,vertices, indice):
    if not esValido(g, vertices, matriz):
        return matriz
    
    if indice == len(vertices):
        return matriz
    
    for i in range(1,10):
        verticeActual = vertices[indice]
        fila = int(verticeActual.split(",")[0])
        columna = int(verticeActual.split(",")[1])  
        matriz[fila][columna] = i
        matriz = resolver_sudoku_bt(g, matriz, vertices, indice+1)
        matriz[fila][columna] = 0
    
    return matriz
        
    

def resolver_sudoku(matriz):
    g = crearGrafoSudoku(matriz)

    vertices = g.obtener_vertices()
    indice = 0

    resolver_sudoku_bt(g, matriz, vertices, indice)
    
    return matriz


matriz = [[0 for _ in range(9)] for _ in range(9)]
resolver_sudoku(matriz)

for i in range(len(matriz)):
    print(matriz[i])