"""
Para ayudar a personas con problemas visuales (por ejemplo, daltonismo) el gobierno de Agrabah decidió 
que en una misma parada de colectivo nunca pararán dos colectivos que usen el mismo color. 
El problema es que ya saben que eso está sucediendo hoy en día, 
así que van a repintar todas las líneas de colectivos. 
Por problemas presupuestarios, desean pintar los colectivos con la menor cantidad posible k colores diferentes. 
Como no quieren parecer un grupo de improvisados que malgasta los fondos públicos, 
quieren hacer un análisis para saber cuál es ese mínimovalor para cumplir con lo pedido 
(pintar cada línea con alguno de los k colores, de tal forma que no hayan dos de mismo color coincidiendo en la misma parada).
Considerando que se tiene la información de todas las paradas de colectivo y qué líneas paran allí, 
modelar el problema utilizando grafos e implementar un algoritmo que determine el mínimo valor k para resolver el problema.
Indicar la complejidad del algoritmo implementado.
"""
import grafo
def pintar_colectivos(colectivos, paradas):
    g = grafo.Grafo()

    if not paradas:
        return 1
    
    for parada in paradas:
        for cole in parada:
            if cole not in g.obtener_vertices():
                g.agregar_vertice(cole)
    
    vertices = g.obtener_vertices()
    arsitas_agregadas = []
    for cole in vertices:
        for parada in paradas:
            if cole in parada:
                for colectivo in parada:
                    if cole == colectivo:
                        continue
                    arista = (cole,colectivo)
                    aristaInv = (colectivo,cole)
                    if arista not in arsitas_agregadas and aristaInv not in arsitas_agregadas:
                        g.agregar_arista(cole,colectivo,1)
                        arsitas_agregadas.append(arista)
                        arsitas_agregadas.append(aristaInv)


    colores = {}

    k = pintar_colectivos_bt(g,vertices,0,1,colores,1,[99999])
    return k

def esCompatible(g,vertices,indice,colores):
    for color in colores:
        if(color == vertices[indice]):
            continue
        elif g.estan_unidos(color, vertices[indice]) and colores[color] == colores[vertices[indice]]:
            return False
    return True

def pintar_colectivos_bt(g,vertices,indice,k,colores,cantColores,kMinimo):
    if indice >= len(vertices):
        if cantColores < kMinimo[0]:
            kMinimo[0] = cantColores
        return
    
    if k > kMinimo[0]:
        return 
    
    colores[vertices[indice]] = k
    cantColores = max(colores.values())
    if esCompatible(g,vertices,indice,colores):
        pintar_colectivos_bt(g,vertices,indice+1,1,colores,cantColores,kMinimo)
        #cantColores = max(colores.values())
    colores.pop(vertices[indice])
    pintar_colectivos_bt(g,vertices,indice,k+1,colores,cantColores,kMinimo)

    return kMinimo[0]


colectivos = ["Línea 1", "Línea 2", "Línea 3", "Línea 4", "Línea 5", "Línea 6", "Línea 7"]
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
#Cole0# 1 4 5
#Cole1# 0 2 5
#Cole2# 1 3
#Cole3# 2 4
#Cole4# 0 3 5 6
#Cole5# 0 1 4 6 
#Cole6# 4 5


#Color1# 0 2 6
#Color2# 1 3 
#Color3# 4
#Color4# 5

print(pintar_colectivos(colectivos,paradas))