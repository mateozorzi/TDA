"""
ej guardias en un tablero nxm, cada guarsia vigila todas las celdas ady. Poner la mayor cantidad de guardias que no vigilen una misma casilla
"""

def agregar_adyacencias(pos, pos_ocupadas, casilleros):
    i = pos[0]
    j = pos[1]

    c_filas = len(casilleros)
    c_col = len(casilleros[0])

    if i > 0:
        pos_ocupadas.add((i-1,j))
    if j > 0:
        pos_ocupadas.add((i,j-1))
    if i < c_filas-1:
        pos_ocupadas.add((i+1,j))
    if j < c_col-1:
        pos_ocupadas.add((i,j+1))
    
    if i > 0 and j > 0:
        pos_ocupadas.add((i-1,j-1))
    if i > 0 and j < c_col-1:
        pos_ocupadas.add((i-1,j+1))
    if i < c_filas-1 and j > 0:
        pos_ocupadas.add((i+1,j-1))
    if i < c_filas-1 and j < c_col-1:
        pos_ocupadas.add((i+1,j+1))
    
    return pos_ocupadas

def guardias(casilleros):
    guardias_colocados = []
    pos_ocupadas = set()


    for i in range(len(casilleros)):
        for j in range(len(casilleros[i])):
            if (i,j) not in pos_ocupadas:
                #agrego el caballero
                pos_ocupadas.add((i,j))
                guardias_colocados.append((i,j))
                pos_ocupadas = agregar_adyacencias((i,j), pos_ocupadas, casilleros)
    
    return guardias_colocados

#regla greedy: recorro los casilleros del castillo, si encuentro una posicion en la que puedo colocoar un guardia lo coloco, si noi puedo colocar
#porque un guardia anterior ya esta vigilando esta casilla, salteo

#Es ipotimo, ya que al colocoar guardias en el primer casillero prosximo posible, minimizo la cantidad de espacios libres
    
