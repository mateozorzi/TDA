import grafo

def agregar_arista_unica(g, nodo1, nodo2, peso=1):
    # Ordenamos los nodos para que siempre se agregue la arista en una dirección fija.
    v1, v2 = sorted([nodo1, nodo2])
    # Suponiendo que el método existe_arista devuelve True si la arista ya existe.
    if not g.existe_arista(v1, v2):
        g.agregar_arista(v1, v2, peso=peso)

def crear_grafo(n=9):
    g = grafo.Grafo()

    # Agregar los nodos (celdas del tablero)
    for fila in range(n):
        for columna in range(n):
            g.agregar_vertice((fila, columna))

    # Agregar las aristas (adyacencias según las reglas del Sudoku)
    for fila in range(n):
        for columna in range(n):
            nodo = (fila, columna)

            # Conectar con las celdas de la misma fila (solo hacia adelante)
            for c in range(columna + 1, n):
                agregar_arista_unica(g, nodo, (fila, c), peso=1)

            # Conectar con las celdas de la misma columna (solo hacia adelante)
            for f in range(fila + 1, n):
                agregar_arista_unica(g, nodo, (f, columna), peso=1)

            # Conectar con las celdas del mismo subgrupo 3x3
            subgrupo_fila = (fila // 3) * 3
            subgrupo_columna = (columna // 3) * 3
            for i in range(subgrupo_fila, subgrupo_fila + 3):
                for j in range(subgrupo_columna, subgrupo_columna + 3):
                    # Para evitar duplicados, solo se agrega si es un nodo posterior
                    if (i, j) != nodo and (i > fila or (i == fila and j > columna)):
                        agregar_arista_unica(g, nodo, (i, j), peso=1)

    return g


def es_compatible(grafo,numeros, fila, col):
    for ady in grafo.adyacentes((fila, col)):
        if ady in numeros:
            if numeros[(fila,col)] == numeros[ady]:
                return False
            
    return True


def resolver_sudoku_bt(matriz,fila,col,numeros, grafo):
    if len(numeros) == len(matriz)*len(matriz[0]):
        return numeros


    if matriz[fila][col] == 0:
        for num in range(1,10):
            numeros[(fila,col)]= num
            if es_compatible(grafo, numeros, fila, col):
                siguiente_fila = fila
                siguiente_col = col + 1
                if siguiente_col == len(matriz[0]):  # Si llegamos al final de la fila
                    siguiente_col = 0
                    siguiente_fila += 1
                numeros = resolver_sudoku_bt(matriz, fila, col, numeros)
                if len(numeros) == len(matriz)*len(matriz[0]):
                    return numeros
        del numeros[(fila, col)]
        matriz[fila][col] = 0
    else:
        # Si la celda ya tiene un número, avanzar a la siguiente celda
        siguiente_fila = fila
        siguiente_col = col + 1
        if siguiente_col == len(matriz[0]):  # Si llegamos al final de la fila
            siguiente_col = 0
            siguiente_fila += 1
        numeros = resolver_sudoku_bt(matriz, fila, col, numeros)
        return numeros

    return None

def cargar_numeros(numeros, matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = numeros[(i,j)]
    return matriz

def resolver_sudoku(matriz):
    numeros = {}

    grafo = crear_grafo(len(matriz))

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:
                numeros[(i,j)] = matriz[i][j]


    numeros = resolver_sudoku_bt(matriz,0,0,numeros, grafo)

    matriz = cargar_numeros(numeros,matriz)

    return matriz

def es_compatible(grafo,numeros, fila, col):
    for ady in grafo.adyacentes((fila, col)):
        if ady in numeros:
            if numeros[(fila,col)] == numeros[ady]:
                return False
            
    return True


def resolver_sudoku_bt(matriz,fila,col,numeros, grafo):
    if len(numeros) == len(matriz)*len(matriz[0]):
        return numeros


    if matriz[fila][col] == 0:
        for num in range(1,10):
            numeros[(fila,col)]= num
            if es_compatible(grafo, numeros, fila, col):
                siguiente_fila = fila
                siguiente_col = col + 1
                if siguiente_col == len(matriz[0]):  # Si llegamos al final de la fila
                    siguiente_col = 0
                    siguiente_fila += 1
                numeros = resolver_sudoku_bt(matriz, fila, col, numeros)
                if len(numeros) == len(matriz)*len(matriz[0]):
                    return numeros
        del numeros[(fila, col)]
        matriz[fila][col] = 0
    else:
        # Si la celda ya tiene un número, avanzar a la siguiente celda
        siguiente_fila = fila
        siguiente_col = col + 1
        if siguiente_col == len(matriz[0]):  # Si llegamos al final de la fila
            siguiente_col = 0
            siguiente_fila += 1
        numeros = resolver_sudoku_bt(matriz, fila, col, numeros)
        return numeros

    return None

def cargar_numeros(numeros, matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = numeros[(i,j)]
    return matriz

def resolver_sudoku(matriz):
    numeros = {}

    grafo = crear_grafo(len(matriz))

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:
                numeros[(i,j)] = matriz[i][j]


    numeros = resolver_sudoku_bt(matriz,0,0,numeros, grafo)

    matriz = cargar_numeros(numeros,matriz)

    return matriz