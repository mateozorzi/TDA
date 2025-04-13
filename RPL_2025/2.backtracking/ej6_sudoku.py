n = 9

def siguiente_pos(matriz, f,c):
    cant_filas = len(matriz)
    cant_col = len(matriz[0])

    if c < cant_col-1:
        c += 1
    else:
        f += 1
        c = 0

    return f,c

def compatible_fila(matriz,f,c):
    num = matriz[f][c]

    for j in range(len(matriz[f])):
        if j == c:
            continue
        if matriz[f][j] == num:
            return False
        
    return True

def compatible_col(matriz,f,c):
    num = matriz[f][c]

    for i in range(len(matriz)):
        if i == f:
            continue
        if matriz[i][c] == num:
            return False
    
    return True

def compatible_subgrupo(matriz,f,c):
    num = matriz[f][c]

    # Calcular las coordenadas del subgrupo 3x3
    subgrupo_fila_inicio = (f // 3) * 3
    subgrupo_col_inicio = (c // 3) * 3

    # Recorrer todas las celdas del subgrupo 3x3
    for i in range(subgrupo_fila_inicio, subgrupo_fila_inicio + 3):
        for j in range(subgrupo_col_inicio, subgrupo_col_inicio + 3):
            if (i == f and j == c):  # Saltar la celda actual
                continue
            if matriz[i][j] == num:  # Si el número ya está en el subgrupo
                return False

    return True

def es_compatible(matriz,f,c):
    if not compatible_fila(matriz,f,c):
        return False
    if not compatible_col(matriz,f,c):
        return False
    if not compatible_subgrupo(matriz,f,c):
        return False
    
    return True

def sudoku_bt(matriz,f,c):
    if f == n:
        return True

    if matriz[f][c] != 0:
        #ya esta seteado, busco sig posicion
        f, c = siguiente_pos(matriz,f,c)
        return sudoku_bt(matriz,f,c)
    
    for i in range(1,10):
        matriz[f][c] = i
        if es_compatible(matriz,f,c):
            f,c = siguiente_pos(matriz,f,c)
            if sudoku_bt(matriz,f,c):
                return True

    matriz[f][c] = 0
    return False


def resolver_sudoku(matriz):
    if sudoku_bt(matriz, 0,0):
        return matriz
    return None



matriz = [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6], [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9]]
print(resolver_sudoku(matriz))