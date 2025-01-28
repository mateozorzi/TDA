"""
Tenemos un set U de n elementos y
un listado de S1,S2,...,Sm de subsets de U.
Un set cover es una coleccion de estos subset, tal que la union es U
Demostrar que set cover es NP-C
"""

"""
Problema de desicion:
SC: "la cantidad de subset <= k', tal que la union de estos da U

VC: "Existe un subconjunto de al menos k elementos, donde para 
cada arista A de la forma (v,w), v o w estan el subconjunto"

QUiero reducir:
VC <=p SC

A partir del grafo, creo el set de U con los aristas de este.
Para construir cada subset, un Si estara representara un nodo y a que aristas esta conectado

Utilizo el mismo k = k', ya que queiro conseguir la cantidad de vertices del VC, que sera igual 
a la cantidad de subset que utilice, ya que cada sub set representa los vertices y las aristas conectadas
Si eligo k' subsets, estare eligiendo k vertices para el subconjunto

Si hay un SC, existe un VC valido?
Si hay a lo sumo k' subconjuntos representando los vertices del grafo, conlas aristas que inciden en estos. 
Si se encontro a lo sumo k subsets, esto representara que habra a lo sumo k vertices que representen un conjunto VC en el grafo

si y solo si

Si hay un VC, existe un SC valido?
Si existen a lo sumo k vertices que generan un VC, en el rblema de subset, como los elementos son
las aristas, se obtendran a los umo k subsets que representaran a los vertices y que cubriran a todas 
las aristas, los elementos del universo.
"""

def validador(U,subset, solucion,k):
    if len(solucion) > k:
        return False
    
    cubierto = [] #creo un set de elementos, con los elemtnos que cubre la solucion
    for subset in solucion: #O(m)
        for elemento in subset: #O(n)
            if elemento not in cubierto:
                cubierto.append(elemento)

    for elemento in U: #O(n)
        if elemento not in cubierto:
            return False

    return True
#Complejidad algoritmo O(m x n) m = cant subset de la solucion
#                               n = cant elementos de la solucion