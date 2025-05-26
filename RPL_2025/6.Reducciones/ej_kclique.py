"""
kclique es NP-C? Reducir IS

1.validador polinomial para k-clique
2.Reducir un problema concoido np-c a k-clique

IS(grafo, k) <= KQ(grafo, k)

is: existe un conjunto de vertices de al menos tamaño k, tal que ninguno sea ady con otro
k-q: existe un dubgrafoi de tamaño al menos k, tal que sea completo

Para la transofrmcaion, tengom una instancia inicial del problema de is, un grafo G y k
Creo un grafo G' con las aristas invertidas, es decri si dos vertices estaban unidos elimino la arista, 
si od svertices no estaba unidos los uno; y k' = k.

Si hay IS hay k-clique
Si en la instancia inicial existe un conjunto valido IS, dada la transofrmacion y la inversion de los vertices, sio existian
al menos k vertices no ady entre si entonces en el grafo G' estos formaran un subgrafo completo tambien de tamaño k, por lo que tambine hay k-clique

si hay k-clique hay IS
Si dada la transformacion, existe un kclique de al menos k vertices, como el grafo G' es una copia de G con las aristas invertidas
los vertices que conforman el subgrafo de k-cliqyue, en el grafo original no estaran unidos entr ellos, por lo que conformaria un is en 
el grafo original.


"""


def validador(grafo, solucion, k):
    if len(solucion) < k:
        return False
    
    for s in solucion:
        if s not in grafo.obtener_vertices():
            return False
        
    for s in solucion:
        for w in solucion:
            if s == w:
                continue
            if not grafo.estan_unidos(s,w):
                return False
            

    return True
#COmplejidad (O(s^2))