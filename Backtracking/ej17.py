"""Se tiene una matriz donde en cada celda hay submarinos, o no, 
y se quiere poner faros para iluminarlos a todos. 
Implementar un algoritmo que dé la cantidad mínima de faros 
que se necesitan para que todos los submarinos queden iluminados, 
siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las diagonales),
y las directamente adyacentes a estas (es decir, un “radio de 2 celdas”)."""
import grafo
# matriz booleana, indica True en las posiciones con submarinos
def submarinos(matriz):
    if not matriz:
        return 0
    g = grafo.Grafo()
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            v = (i,j)
            g.agregar_vertice(v)
    # Agregar aristas según las adyacencias de los faros
    for v in g.obtener_vertices():
        x, y = v
        for i in range(x - 2, x + 3):
            for j in range(y - 2, y + 3):
                 if 0 <= i < len(matriz) and 0 <= j < len(matriz[0]) and (i, j) != v and not g.estan_unidos(v,(i,j)):
                    g.agregar_arista(v, (i, j),1)

    colocados = 0
    faros = []
    minimo = [0]
    minimo, faros = cant_minima_de_faros_bt(g,matriz,g.obtener_vertices(),0,colocados,minimo,faros)
    print(faros)
    return minimo[0]

def cant_minima_de_faros_bt(g,matriz,vertices,indice,colocados,minimo,faros):
    if colocados > minimo[0] and minimo[0] > 0:
        return
    if((colocados < minimo[0] or minimo[0] == 0) and estaCubierto(g,matriz,faros) and esCompatible(g,matriz,faros)): #esta completo?????
        minimo[0] = colocados
    
    if indice >= len(vertices):
        return

    if not esCompatible(g,matriz,faros):
        return

    faros.append(vertices[indice])
    cant_minima_de_faros_bt(g,matriz,vertices,indice+1,colocados+1,minimo,faros)
    faros.remove(vertices[indice])
    cant_minima_de_faros_bt(g,matriz,vertices,indice+1,colocados,minimo,faros)

    return minimo,faros

def esCompatible(g,matriz,faros):
    for faro in faros:
        x,y = faro
        if matriz[x][y] == True:
            return False
        ady = any(matriz[x][y] == True for x,y in g.adyacentes(faro))
        if not ady:
            return False
        
    return True

def estaCubierto(g,matriz,faros):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]:
                cubierto = any((i, j) in g.adyacentes(faro) for faro in faros)
                if not cubierto:
                    return False
    return True

matriz_submarinos = [
    [True, False, False, False, False, True],
    [False, False, False, False, False, False],
    [False, False, True, True, False, False],
    [False, False, True, True, False, False],
    [False, False, False, False, False,False],
    [True, False, False, False,False, True]
]

print(submarinos(matriz_submarinos))