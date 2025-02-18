"""
H-C: Dado un grafo G y un numero K, es posivle ghacer que G tenga un cicloH si se le agregan a los sumo k aristas?

1. validador polinomial, comprueba que esta en NP
2.Reduccion de cicloH a H-C, para prbar que NP-C

cicloH: Dado un grafo G', existe un ciclo que pase una uinica que vez por todos los vertices del grafo?

Reduccion:
cicloH(G') <=p H-C(G, k)

Para la reduccion se realiza una transofmacion de la instancia de cicloH para que la caja
negra que resuelve H-C.
Hacemos una copia del grafo G' == G
y a k le damos el valor de 0. k == 0, esto para que no agregue ningun vertice nuevo

Si hay cicloH haty H-C:
Si en G' exisrte un ciclo que pasa una unica vez por cada vertice del grafo, entonces
dado la transoformacion de la reduccion. En G habra un ciclo si se le agrega la cantiad de vertices
dicha por k, en este caso como es 0 no se agregan nuevos vertices, por lo que si ya en G' habia un ciclo,
en G tambien lo habra

si hay H-C hay cicloH:
Si se ecuentra un ciclo dada la instancia de H-C, entonces como G es una copia del grafo orignal G' y
al valor de k se le asigno 0, no se agregan nuevos vertices, entonces en G' existira un ciclo que pase una
uniuca vez por cada verice.

"""

def validador(grafo, k, agregados, ciclo):
    if len(agregados) > k:
        return False
    
    
    #compruebo que hay un ciclo
    if ciclo[0] != ciclo[-1]:
       return False
    
    setVertices = set(grafo.obtener_vertices())
    visitados = set()
    for i in range(1, len(ciclo)):
        if ciclo[i] not in setVertices or ciclo[i-1] not in setVertices:
            return False
        if not grafo.estan_unidos(ciclo[i-1], ciclo[i]):
            return False
        if ciclo[i] in visitados:
            return False
        visitados.add(ciclo[i])

    return True
