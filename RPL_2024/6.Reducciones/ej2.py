"""
El problema del Vertex Cover se define como: dado un grafo no dirigido, 
obtener el mínimo subconjunto de vértices del grafo tal que 
toda arista del grafo tenga al menos uno de sus vértices perteneciendo al subconjunto. 
Dicho conjunto es un Vertex Cover. 
Definir el problema de decisión del Vertex Cover. 
Luego, implementar un verificador polinomial para este problema. 
¿Cuál es la complejidad del verificador implementado? Justificar
"""

"""
Solucion:

VC(grafo,k) -> True, si existe un subconjunto de al menos k elementos, en el que
                se tengan cubiertas todas las aritas del grafo
            -> False, sino
Verificador: verifica que la solucion tenga al menos k elementos, verificar que esten todas las aristas recorridas
                y que los aristas no esten conectadas
"""

def verificadorVC(grafo,k,solucion):
    #me fijo que tenfa al menos k elementos
    if len(solucion) < k: #O(1)
        return False
    
    for v in solucion:
        if v not in grafo.vertices(): #O(len(solucion) * V)
            return False
        
    #me fijo que cubra todas las aristas       
    for i in grafo.vertices:
        for j in grafo.adyacentes(i): #O(len(adyacentes) * V)
            if i not in solucion and j not in solucion: 
                return False
    
    #como V >= len(solucion) y V > len(adyacentes), el pero de los casos tendra
    #complejidad O(V^2)

    return True