"""
Para ayudar a personas con problemas visuales (por ejemplo, daltonismo) el gobierno de Agrabah decidió que en una misma parada de colectivo nunca pararán dos colectivos que usen el mismo color. El problema es que ya saben que eso está sucediendo hoy en día, así que van a repintar todas las líneas de colectivos. Por problemas presupuestarios, desean pintar los colectivos con la menor cantidad posible k colores diferentes. Como no quieren parecer un grupo de improvisados que malgasta los fondos públicos, quieren hacer un análisis para saber cuál es ese mínimovalor para cumplir con lo pedido (pintar cada línea con alguno de los k colores, de tal forma que no hayan dos de mismo color coincidiendo en la misma parada). Considerando que se tiene la información de todas las paradas de colectivo y qué líneas paran allí, modelar el problema utilizando grafos e implementar un algoritmo que determine el mínimo valor k para resolver el problema. Indicar la complejidad del algoritmo implementado.

Nota: el ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo, está disponible como se describe.
"""
import grafo

def modelar(colectivos, paradas):
    g = grafo.Grafo()

    for c in colectivos:
        g.agregar_vertice(c)
    
    for p in paradas:
        for c1 in p:
            for c2 in p:
                if c1 == c2:
                    continue
                if not g.estan_unidos(c1,c2):
                    g.agregar_arista(c1,c2,1)
    
    return g

def es_compatible(grafo, actual, colores):
    for ady in grafo.adyacentes(actual):
        if ady in colores:
            if colores[ady] == colores[actual]:
                return False
    
    return True

def pintar_bt(grafo, colectivos, indice, colores, k, minimo):
    if indice >= len(colectivos):
        cantColores = max(colores.values())
        if cantColores < minimo[0]:
            minimo[0] = cantColores
        return colores, minimo
    
    if k > minimo[0]:
        return colores, minimo
    
    colores[colectivos[indice]] = k
    if es_compatible(grafo, colectivos[indice], colores):
        colores, minimo = pintar_bt(grafo, colectivos, indice+1, colores, 1, minimo)
    del colores[colectivos[indice]]
    colores, minimo = pintar_bt(grafo,colectivos, indice, colores,k+1, minimo)

    return colores, minimo


def pintar_colectivos(colectivos, paradas):
    k = 1
    colores = {}

    indice = 0
    minimo = [len(colectivos)]

    grafo = modelar(colectivos, paradas)

    colores, minimo = pintar_bt(grafo, colectivos, indice, colores, k, minimo)

    cantColores = 1
    for colectivos in colores:
        if colores[colectivos] > cantColores:
            cantColores = colores[colectivos]
    return minimo[0]


colectivos = [0, 1, 2, 3, 4, 5, 6]
paradas = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 4],
    [0, 4],
    [4 ,5],
    [4, 6],
    [5 ,6],
    [0 ,5],
    [1 ,5]
]

print(pintar_colectivos(colectivos, paradas))