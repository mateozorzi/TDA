def noVigilada(matriz, fila, col):
    if fila > 0 and matriz[fila-1][col] == 'G':
        return False
    if col > 0 and matriz[fila][col-1] == 'G':
        return False
    if fila < len(matriz)-1 and matriz[fila+1][col] == 'G':
        return False
    if col < len(matriz[0])-1 and matriz[fila][col+1] == 'G':
        return False
    
    if fila > 0 and col > 0 and matriz[fila-1][col-1] == 'G':
        return False
    if fila > 0 and col < len(matriz[0])-1 and matriz[fila-1][col+1] == 'G':
        return False
    if fila < len(matriz)-1 and col > 0 and matriz[fila+1][col-1] == 'G':
        return False
    if fila < len(matriz)-1 and col < len(matriz[0])-1 and matriz[fila+1][col+1] == 'G':
        return False
 
    return True

# matriz de n x m, "-" casillero vacio, "G" casillero con guardia
def castillo(matriz, n, m):
    cantGuardias = 0

    #Regla greedy, ir casillero x casillero viendo si es posible agregar un guardia (optimo local),
    #comprobando las adyacencias ady de cada casillero

    for fila in range(len(matriz)):
        for col in range(len(matriz[fila])):
            if matriz[fila][col] == '-' and noVigilada(matriz, fila, col):
                matriz[fila][col] = 'G'
                cantGuardias += 1

    return cantGuardias, matriz