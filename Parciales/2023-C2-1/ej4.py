"""
IS: Dado un grafo, existen al menos k vertices que formne un connjunto no adyacentes entre si?

PS: Dado un grafo drigido y set de pedidos P ( camino dentro del grafo), exiten al menos k pedidos que no tengan
vertices en comun?

Para probar que IS es NP-C
1. validador polinomial de IS, para comprobar que forma parte de NP
2. Reducir un problema NP-C a IS

Reduccion:
PS(grafoD, P, k) <=p IS(grafo', k')
Para la transformacion de la reduccion:
Creo un nuevo grafo no dirigo grafo', creo un vertice por cada camino del set
y creo las arsitas segun los caminos que tengan vertices en comun
el valor de k sera el mismo que k' ya que buscamos al menos k camino indep que serian
en el nuevo grafo k' vertices independientes

Si hay PS hay IS:
Si hay al menos k pedidos que no compartan vertices, entonces en grafo' existira un conjunto
de al menos k vertices donde no sean ady entre si, esto porque cada vertice representa un camino del set. Por 
loq eu si dos pedidos son independientes, estos veritices tambien lo seran

Si hay IS hay PS:
SI existe en grafo' un conjunto k de vertices indepdneites entre si, como cada uno de estos vertices simboliza un camino del set 
original, entonces en la instancia de PS existiran al menos k pedidos que no compartas vertices entre si. Ya que cada vertice
de la transformacion represnta un pedidos distnto, si dos vertices son indendientes, esos dos caminos tambien lo seran. 
Por lo que si hay dos camino no son adyacentes entre si, entonces estos pedidos perteneceran al conjunto.


"""

def validador(grafo, k, solucion):
    if len(solucion) < k:
        return False
    
    for v in solucion:
        for w in solucion:
            if v == w:
                continue
            if grafo.estan_unidos(v,w):
                return False
            
    return True