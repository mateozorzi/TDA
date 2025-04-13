"""
Quiero demostrar que k_clique es NP_Completo
Para esto debo:
1. Demostrar que k clique es NP -> validador polinomial
2. buscra reducir un problema que yo conozca que sea NP-C a k clique.

Para demostrar que k clique es NP-C, elijo un problema NP-C al que voy a reducir a k clique
Independent Set en su forma de probblema de decision es NP-C
IS = Dado un grafo, existe un conjunto de vertices de al menos tamaño k, tal que no son adyacentes entre si

k clique en su forma de problema de decision es:
kC: Dado un grafo, existe un subgrafo completo de tamaño k

Quiero demostrar que IS(grafo,k) <=p kC(grafo_,k)
Tengo una caja negra que resuelve el problema de k_clique. Tengo que adecuar el problema de IS, en pasos polinomicos,
para que lo pueda resolver k_clique.
A partir del grafo original, creo una copia donde invierto las adyacencias de los vertices. Uniendo todos los vertices que no son adyacentes entre si.

-----
SI HAY IS, HAY K-C
Si existe un IS de al menos tamaño k en el grafo original, existira un k clique en el grafo_ dado que este se creo dada una copia del
grafo original, pero inviertiendo las adyacencias de todo el grafo. Entonces los vertices que antes eran independientes
ahora formaran un subgrafo de tamaño k. Dado que se inviertiron las adyacencias de grafo original en la reduccion, no puede quedar
en este nuevo grafo un par de vertices que si antes no eran adyacentes, ahora tampoco lo sean. Ya que seria absurdo porque se inviertorn todas las ady.
-----
SI HAY K-C, HAY IS
Si hay un k clique de tamaño k en el nuevo grafo_, y dado que es el resultado de la reduccion especificada, entonces
se puede entender que al revertir las adyacencias de los vertices, donde antes se formaba un subgrafo completo de tamaño k,
ahora esos mismos vertices estaran formando un conjunto independiento de tamaño k en el grafo original. Un vertice que pertencia 
al grafo donde habi un k-clique, al revertir las adyacencias no puede quedar adyacente a otro vertice que tambien pertenecia al
subgrafo completo de grafo_, lo contrario indicaria que el reultado de k_clique no es valido, lo cual es absurdo.
"""

def validador(grafo, solucion, k):
    if not solucion:
        return False
    if len(solucion) != k:
        return False
    
    for v in solucion:
        for w in solucion:
            if v != w and not grafo.estan_unidos(v,w):
                return False
            continue #el mismo vertice
    
    return True