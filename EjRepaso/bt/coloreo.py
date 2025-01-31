import grafo

def esValido(grafo, vertices, colores,color, indice):
    adyacentes = grafo.adyacentes(vertices[indice])
    for ady in adyacentes:
        if ady in colores[color]:
            return False
    
    return True

def coloreo_bt(grafo, vertices, colores, indice,k, solucion):  
    if indice == len(vertices):
        return colores
    
    for color in range(k): 
        if esValido(grafo, vertices, colores, color, indice):
            colores[color].add(vertices[indice])
            colores = coloreo_bt(grafo, vertices, colores, indice+1, k, solucion)
            return colores
    
    return None

def coloreo(grafo, k):
    vertices = grafo.obtener_vertices()
    indice = 0

    colores = {_ : set() for _ in range(k)}

    solucion = {_ : set() for _ in range(k)}

    colores = coloreo_bt(grafo, vertices, colores, indice, k, solucion)
    return colores


g = grafo.Grafo()
g.agregar_vertice(1)
g.agregar_vertice(2)
g.agregar_vertice(3)
g.agregar_vertice(4)
g.agregar_vertice(5)

g.agregar_arista(1,2)
g.agregar_arista(1,3)
g.agregar_arista(2,4)
g.agregar_arista(2,3)
g.agregar_arista(5,4)

print(coloreo(g,5)) # Debería imprimir algo como {1: {1, 3, 5}, 2: {2, 4}} o similar
