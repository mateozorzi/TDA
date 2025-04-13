"""
El problema del Independent Set se define como: dado un grafo no dirigido, 
obtener el máximo subconjunto de vértices del grafo tal que ningun par de vértices del subconjunto sea adyacente entre si. 
Dicho conjunto es un Independet Set. Definir el problema de decisión del Independent Set. 
Luego, implementar un verificador polinomial para este problema. 
¿Cuál es la complejidad del verificador implementado? Justificar
"""

"""
Solucion:
IS(grafo, k)    -> True, existe un subgrupo de al menos k elementos no adyacentes
                -> False, no existe un subgrupo de al menos k elementos no adyacentes
Verficador polinomial:  Compruebo que exista el grafo, que la solucion tenga al menos k elementos.
                        y que los vertices de la solucion no esten conectados
                        Debe ser capaz de determinar si la solucion es valida o no.
"""

def verificadorIS(grafo,k,solucion):
    if len(solucion) < k: #O(1)
        return False
    
    for v in solucion: #O(len(solucion) * V) -> V >= len(solucion)
        if v not in grafo.vertices():
            return False
        
    for i in solucion:    #O(len(solucion)^2)
        for w in solucion:
            if i == w:
                continue
            if grafo.hay_arista(i,w):
                return False
    #En el peor de los casos debo recorrer todos los vertices
    #La complejidad sera O(V^2) 
    return True